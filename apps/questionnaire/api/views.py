from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.views import LogUserMixin
from .serializers import QuestionnaireSerializer
from ..models import Questionnaire, STATUSES


class QuestionnaireViewSet(LogUserMixin, viewsets.ReadOnlyModelViewSet):
    """
    List and detail view for questionnaires.

    Filters can be passed in the url, e.g. /en/api/v1/questionnaire/?version=1

    Following fields can be filtered for:
    - version

    The results are displayed in the same language as the request. The language
    of the results can alternatively be set by setting the query string 'lang',
    e.g. ?lang=fr

    """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionnaireSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('version', )

    def get_queryset(self):
        """
        Filter valid questionnaires; Status "3" is public.
        """
        return Questionnaire.objects.filter(
            status=STATUSES[3][0]
        )
