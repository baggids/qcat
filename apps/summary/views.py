import contextlib
import logging
from os.path import join, isfile

from django.conf import settings
from django.db.models import Q
from django.http import Http404
from django.utils.translation import get_language

from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse

from configuration.cache import get_configuration
from questionnaire.models import Questionnaire
from questionnaire.utils import get_query_status_filter, \
    get_questionnaire_data_in_single_language
from summary.renderers import TechnologyFullSummaryRenderer, \
    ApproachesFullSummaryRenderer

logger = logging.getLogger(__name__)


class CachedPDFTemplateResponse(PDFTemplateResponse):
    """
    Creating the pdf includes two resource-heavy processes:
    - extracting the json to markup (frontend)
    - call to wkhtmltopdf (backend)

    Therefore, the content is created only once per filename (which should
    distinguish between new questionnaire edits). This only works with
    reasonably precise file names!
    """

    @property
    def rendered_content(self):
        file_path = join(settings.SUMMARY_PDF_PATH, self.filename)
        if isfile(file_path):
            # Catch any exception, worst case is that the pdf is created from
            # scratch again
            with contextlib.suppress(Exception) as e:
                return open(file_path, 'rb').read()

        content = super().rendered_content
        with contextlib.suppress(Exception) as e:
            open(file_path, 'wb').write(content)

        return content


class SummaryPDFCreateView(PDFTemplateView):
    """
    Put the questionnaire data to the context and return the rendered pdf.
    """
    response_class = CachedPDFTemplateResponse
    summary_type = 'full'  # Only one summary type is available right now
    base_template_path = 'summary/'
    http_method_names = ['get']
    render_classes = {
        'technologies': {'full': TechnologyFullSummaryRenderer},
        'approaches': {'full': ApproachesFullSummaryRenderer}
    }
    footer_template = '{}layout/footer.html'.format(base_template_path)
    # see: http://wkhtmltopdf.org/usage/wkhtmltopdf.txt
    cmd_options = {
        'dpi': '96',
        'margin-top': '1cm',
        'margin-bottom': '1cm',
    }
    default_quality = 'screen'

    def get(self, request, *args, **kwargs):
        self.questionnaire = self.get_object(questionnaire_id=self.kwargs['id'])
        try:
            self.code = self.questionnaire.configurations.filter(
                active=True
            ).first().code
        except AttributeError:
            raise Http404
        self.config = get_configuration(configuration_code=self.code)
        self.quality = self.request.GET.get('quality', self.default_quality)
        # filename is set withing render_to_response, this is too late as it's
        # used for caching.
        self.filename = self.get_filename()
        return super().get(request, *args, **kwargs)

    def get_template_names(self):
        template = self.request.GET.get('template', self.code)
        return '{}/layout/{}.html'.format(self.base_template_path, template)

    def get_filename(self) -> str:
        """
        The filename is specific enough to be used as 'pseudo cache-key' in the
        CachedPDFTemplateResponse.
        """
        return 'wocat-{identifier}-{language}-{summary_type}-{quality}-' \
               'summary-{update}.pdf'.format(
            identifier=self.questionnaire.id,
            language=get_language(),
            summary_type=self.summary_type,
            quality=self.quality,
            update=self.questionnaire.updated.strftime('%Y-%m-%d-%H-%M')
        )

    def get_object(self, questionnaire_id: int) -> Questionnaire:
        """
        Get questionnaire and check status / permissions.
        """
        status_filter = get_query_status_filter(self.request)
        status_filter &= Q(id=questionnaire_id)
        obj = Questionnaire.with_status.not_deleted().filter(
            Q(id=questionnaire_id), status_filter
        ).distinct()
        if not obj.exists() or obj.count() != 1:
            raise Http404
        return obj.first()

    def get_summary_data(self, **data):
        """
        Get summary data from renderer according to configuration.
        """
        try:
            renderer = self.render_classes[self.config.keyword][self.summary_type]
        except KeyError:
            raise Http404
        return renderer(
            config=self.config,
            questionnaire=self.questionnaire,
            quality=self.quality,
            base_url=self.request.build_absolute_uri('/'), **data
        ).data

    def get_prepared_data(self, questionnaire: Questionnaire) -> dict:
        """
        Load the prepared JSON for given object in the current language.
        """
        data = get_questionnaire_data_in_single_language(
            questionnaire_data=questionnaire.data,
            locale=get_language(),
            original_locale=questionnaire.original_locale
        )
        return self.get_summary_data(**data)

    def get_footer_context(self) -> dict:
        """
        Provide variables used in the footer template.
        """
        name = self.questionnaire.get_name()
        if len(name) > 70:
            name = '{}...'.format(name[:67])
        return {
            'footer_name': name,
            'footer_config': self.code.title()
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['block'] = self.get_prepared_data(self.questionnaire)
        context.update(self.get_footer_context())
        return context
