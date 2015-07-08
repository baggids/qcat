import json
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http.response import HttpResponse
from django.test.client import RequestFactory
from unittest.mock import patch, Mock

from accounts.tests.test_authentication import (
    create_new_user,
)
from configuration.configuration import (
    QuestionnaireConfiguration,
    QuestionnaireCategory,
    QuestionnaireSection,
)
from qcat.tests import TestCase
from qcat.utils import session_store
from questionnaire.models import Questionnaire, File
from questionnaire.views import (
    generic_file_upload,
    generic_questionnaire_details,
    generic_questionnaire_link_form,
    generic_questionnaire_link_search,
    generic_questionnaire_list,
    generic_questionnaire_new,
    generic_questionnaire_new_step,
)
from sample.tests.test_views import (
    get_section_count,
    get_valid_new_step_values,
    get_valid_new_values,
    get_valid_details_values,
    get_valid_list_values,
    get_valid_link_form_values,
    route_questionnaire_details,
    route_questionnaire_list,
    route_questionnaire_link_search,
)

file_upload_route = 'file_upload'
file_display_route = 'file_serve'
valid_file = 'static/assets/img/img01.jpg'
invalid_file = 'bower.json'  # Needs to exist but not valid file type


class GenericQuestionnaireLinkFormTest(TestCase):

    fixtures = ['groups_permissions.json', 'sample.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.url = '/sample/edit/links'
        self.request = self.factory.get(self.url)
        self.request.user = create_new_user()
        session_store.clear()

    def test_requires_login(self):
        self.client.logout()
        res = self.client.post(self.url, follow=True)
        self.assertTemplateUsed(res, 'login.html')

    @patch.object(QuestionnaireConfiguration, 'get_links_configuration')
    @patch.object(QuestionnaireConfiguration, '__init__')
    def test_creates_questionnaire_configuration(
            self, mock_QuestionnaireConfiguration,
            mock_QuestionnaireConfiguration_get_links_configuration):
        mock_QuestionnaireConfiguration.return_value = None
        mock_QuestionnaireConfiguration_get_links_configuration.return_value \
            = []
        generic_questionnaire_link_form(
            self.request, *get_valid_link_form_values()[0],
            **get_valid_link_form_values()[1])
        mock_QuestionnaireConfiguration.assert_called_once_with('sample')

    @patch.object(QuestionnaireConfiguration, 'get_links_configuration')
    @patch.object(QuestionnaireConfiguration, '__init__')
    def test_calls_get_links_configuration(
            self, mock_QuestionnaireConfiguration,
            mock_get_links_configuration):
        mock_QuestionnaireConfiguration.return_value = None
        mock_get_links_configuration.return_value \
            = []
        generic_questionnaire_link_form(
            self.request, *get_valid_link_form_values()[0],
            **get_valid_link_form_values()[1])
        mock_get_links_configuration.assert_called_once_with()

    @patch('questionnaire.views.get_session_questionnaire')
    def test_calls_get_session_questionnaire(
            self, mock_get_session_questionnaire):
        mock_get_session_questionnaire.return_value = {}, {}
        generic_questionnaire_link_form(
            self.request, *get_valid_link_form_values()[0],
            **get_valid_link_form_values()[1])
        mock_get_session_questionnaire.assert_called_once_with('sample')

    @patch('questionnaire.views.render')
    def test_calls_render(self, mock_render):
        generic_questionnaire_link_form(
            self.request, *get_valid_link_form_values()[0],
            **get_valid_link_form_values()[1])
        mock_render.assert_called_once_with(self.request, 'form/links.html', {
            'valid': True,
            'overview_url': '/en/sample/edit/#links',
            'link_forms': [(
                {'label': 'samplemulti', 'keyword': 'samplemulti'}, []
            )],
            'configuration_name': 'sample',
            'title': 'SAMPLE Links'
        })


class GenericQuestionnaireLinkSearchTest(TestCase):

    fixtures = ['sample.json', 'sample_questionnaires.json']

    @patch.object(QuestionnaireConfiguration, '__init__')
    def test_creates_questionnaire_configuration(self, mock_Conf):
        mock_Conf.return_value = None
        generic_questionnaire_link_search(Mock(), 'sample')
        mock_Conf.assert_called_once_with('sample')

    @patch('questionnaire.views.QuestionnaireConfiguration')
    @patch('questionnaire.views.query_questionnaires_for_link')
    def test_calls_query_questionnaires_for_link(self, mock_query, mock_Conf):
        mock_Conf.get_list_data.return_value = []
        mock_query.return_value = 0, []
        mock_request = Mock()
        generic_questionnaire_link_search(mock_request, 'sample')
        mock_query.assert_called_once_with(mock_Conf(), mock_request.GET.get())

    def test_returns_empty_if_no_q(self):
        req = RequestFactory().get(reverse(route_questionnaire_link_search))
        ret = generic_questionnaire_link_search(req, 'sample')
        j = json.loads(ret.content.decode('utf-8'))
        self.assertEqual(j, {})

    def test_returns_empty_if_no_results(self):
        req = RequestFactory().get(reverse(route_questionnaire_link_search))
        req.GET = {'q': 'foo'}
        ret = generic_questionnaire_link_search(req, 'sample')
        j = json.loads(ret.content.decode('utf-8'))
        self.assertEqual(j, {"total": 0, "data": []})

    def test_returns_results(self):
        req = RequestFactory().get(reverse(route_questionnaire_link_search))
        req.GET = {'q': 'key'}
        ret = generic_questionnaire_link_search(req, 'sample')
        j = json.loads(ret.content.decode('utf-8'))
        self.assertEqual(j.get('total'), 2)
        data = j.get('data')
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 5)
        self.assertEqual(data[0].get('code'), 'sample_1')
        self.assertIn('display', data[0])
        self.assertEqual(data[0].get('id'), 1)
        self.assertEqual(data[0].get('name'), 'Sample Key 1a')
        self.assertEqual(data[0].get('value'), 1)
        self.assertEqual(len(data[1]), 5)
        self.assertEqual(data[1].get('code'), 'sample_2')
        self.assertIn('display', data[1])
        self.assertEqual(data[1].get('id'), 2)
        self.assertEqual(data[1].get('name'), 'Sample Key 1b')
        self.assertEqual(data[1].get('value'), 2)


class GenericQuestionnaireNewStepTest(TestCase):

    fixtures = ['groups_permissions.json', 'sample.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/sample/new/cat_1')
        self.request.user = create_new_user()
        session_store.clear()

    @patch.object(QuestionnaireConfiguration, '__init__')
    @patch.object(QuestionnaireConfiguration, 'get_category')
    def test_creates_questionnaire_configuration(
            self, mock_QuestionnaireConfiguration_get_category,
            mock_QuestionnaireConfiguration):
        mock_QuestionnaireConfiguration.return_value = None
        mock_QuestionnaireConfiguration_get_category.return_value = None
        with self.assertRaises(Http404):
            generic_questionnaire_new_step(
                self.request, 'cat_1', 'sample', 'template', 'route')
        mock_QuestionnaireConfiguration.assert_called_once_with('sample')

    @patch.object(QuestionnaireConfiguration, 'get_category')
    def test_gets_category(self, mock_get_category):
        mock_get_category.return_value = None
        with self.assertRaises(Http404):
            generic_questionnaire_new_step(
                self.request, 'cat_1', 'sample', 'template', 'route')
        mock_get_category.assert_called_once_with('cat_1')

    @patch('questionnaire.views.get_session_questionnaire')
    def test_calls_get_session_questionnaire(
            self, mock_get_session_questionnaire):
        mock_get_session_questionnaire.return_value = {}, {}
        generic_questionnaire_new_step(
            self.request, *get_valid_new_step_values()[0])
        mock_get_session_questionnaire.assert_called_once_with('sample')

    @patch('questionnaire.views.get_questionnaire_data_for_translation_form')
    def test_calls_get_questionnaire_data_for_translation_form(
            self, mock_get_questionnaire_data):
        generic_questionnaire_new_step(
            self.request, *get_valid_new_step_values()[0])
        mock_get_questionnaire_data.assert_called_once_with({}, 'en', None)

    @patch.object(QuestionnaireCategory, 'get_form')
    def test_calls_category_get_form(self, mock_get_form):
        mock_get_form.return_value = None, None
        generic_questionnaire_new_step(
            self.request, *get_valid_new_step_values()[0])
        mock_get_form.assert_called_once_with(
            post_data=None, show_translation=False, initial_data={})

    @patch.object(messages, 'success')
    @patch.object(QuestionnaireCategory, 'get_form')
    @patch('questionnaire.views.save_session_questionnaire')
    def test_form_submission_saves_form(
            self, mock_save_session_questionnaire, mock_get_form,
            mock_messages):
        mock_get_form.return_value = None, []
        r = self.request
        r.method = 'POST'
        generic_questionnaire_new_step(
            r, *get_valid_new_step_values()[0])
        mock_save_session_questionnaire.assert_called_once_with(
            'sample', {}, {})

    @patch.object(QuestionnaireCategory, 'get_form')
    @patch('questionnaire.views.render')
    def test_calls_render(self, mock_render, mock_get_form):
        mock_get_form.return_value = "foo", "bar"
        generic_questionnaire_new_step(
            self.request, *get_valid_new_step_values()[0])
        mock_render.assert_called_once_with(
            self.request, 'form/category.html', {
                'category_formsets': "bar",
                'category_config': "foo",
                'title': 'QCAT Form',
                'overview_url': '/en/sample/edit/#cat_0',
                'valid': True,
                'configuration_name': 'sample',
            })

    def test_returns_rendered_response(self):
        ret = generic_questionnaire_new_step(
            self.request, *get_valid_new_step_values()[0])
        self.assertIsInstance(ret, HttpResponse)


class GenericQuestionnaireNewTest(TestCase):

    fixtures = ['groups_permissions.json', 'sample.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/sample/new')
        self.request.user = create_new_user()

    @patch.object(QuestionnaireConfiguration, '__init__')
    @patch.object(QuestionnaireConfiguration, 'get_details')
    def test_creates_questionnaire_configuration(
            self, mock_QuestionnaireConfiguration_get_details,
            mock_QuestionnaireConfiguration):
        mock_QuestionnaireConfiguration.return_value = None
        # with self.assertRaises(AttributeError):
        generic_questionnaire_new(
            self.request, *get_valid_new_values()[0],
            **get_valid_new_values()[1])
        mock_QuestionnaireConfiguration.assert_called_once_with('sample')

    @patch('questionnaire.views.get_session_questionnaire')
    def test_calls_get_session_questionnaire(
            self, mock_get_session_questionnaire):
        mock_get_session_questionnaire.return_value = {}, {}
        generic_questionnaire_new(
            self.request, *get_valid_new_values()[0],
            **get_valid_new_values()[1])
        mock_get_session_questionnaire.assert_called_once_with('sample')

    @patch('questionnaire.views.QuestionnaireConfiguration')
    @patch('questionnaire.views.clean_questionnaire_data')
    @patch('questionnaire.models.put_questionnaire_data')
    def test_calls_clean_questionnaire_data(
            self, mock_put_data, mock_clean_questionnaire_data,
            mock_QuestionnaireConfiguration):
        mock_put_data.return_value = None, None
        mock_clean_questionnaire_data.return_value = {"foo": "bar"}, []
        r = self.request
        r.method = 'POST'
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_clean_questionnaire_data.assert_called_once_with(
            {}, mock_QuestionnaireConfiguration())

    @patch.object(messages, 'info')
    def test_adds_message_if_empty(self, mock_messages_info):
        r = self.request
        r.method = 'POST'
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_messages_info.assert_called_once_with(
            r, '[TODO] You cannot submit an empty questionnaire',
            fail_silently=True)

    @patch('questionnaire.views.redirect')
    def test_redirects_to_same_path_if_empty(self, mock_redirect):
        r = self.request
        r.method = 'POST'
        r.path = 'foo'
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_redirect.assert_called_once_with('foo')

    @patch.object(Questionnaire, 'create_new')
    @patch('questionnaire.views.clean_questionnaire_data')
    def test_calls_create_new_questionnaire(
            self, mock_clean_questionnaire_data, mock_create_new):
        r = self.request
        r.method = 'POST'
        mock_clean_questionnaire_data.return_value = {"foo": "bar"}, []
        mock_create_new.return_value = Mock()
        mock_create_new.return_value.id = 1
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_create_new.assert_called_once_with('sample', {})

    @patch('questionnaire.views.clear_session_questionnaire')
    @patch('questionnaire.views.clean_questionnaire_data')
    @patch('questionnaire.models.put_questionnaire_data')
    def test_calls_clear_session_questionnaire(
            self, mock_put_data, mock_clean_questionnaire_data,
            mock_clear_session_questionnaire):
        mock_put_data.return_value = None, None
        r = self.request
        r.method = 'POST'
        mock_clean_questionnaire_data.return_value = {"foo": "bar"}, []
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_clear_session_questionnaire.assert_called_once_with(
            configuration_code='sample')

    @patch.object(messages, 'success')
    @patch('questionnaire.views.clean_questionnaire_data')
    @patch('questionnaire.models.put_questionnaire_data')
    def test_adds_message(
            self, mock_put_data, mock_clean_questionnaire_data,
            mock_messages_sucess):
        mock_put_data.return_value = None, None
        r = self.request
        r.method = 'POST'
        mock_clean_questionnaire_data.return_value = {"foo": "bar"}, []
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_messages_sucess.assert_called_once_with(
            r, '[TODO] The questionnaire was successfully created.',
            fail_silently=True)

    @patch('questionnaire.views.redirect')
    @patch.object(Questionnaire, 'create_new')
    @patch('questionnaire.views.clean_questionnaire_data')
    def test_redirects_to_success_route(
            self, mock_clean_questionnaire_data,
            mock_create_new, mock_redirect):
        r = self.request
        r.method = 'POST'
        mock_clean_questionnaire_data.return_value = {"foo": "bar"}, []
        mock_create_new.return_value = Mock()
        mock_create_new.return_value.id = 1
        generic_questionnaire_new(
            r, *get_valid_new_values()[0], **get_valid_new_values()[1])
        mock_redirect.assert_called_once_with(
            'sample:questionnaire_details', 1)

    @patch('questionnaire.views.get_questionnaire_data_in_single_language')
    def test_calls_get_questionnaire_data_in_single_language(
            self, mock_get_questionnaire_data):
        generic_questionnaire_new(
            self.request, *get_valid_new_values()[0],
            **get_valid_new_values()[1])
        mock_get_questionnaire_data.assert_called_once_with({}, 'en')

    @patch.object(QuestionnaireConfiguration, 'get_details')
    def test_calls_get_details(self, mock_get_details):
        generic_questionnaire_new(
            self.request, *get_valid_new_values()[0],
            **get_valid_new_values()[1])
        mock_get_details.assert_called_once_with(
            {}, editable=True, edit_step_route='sample:questionnaire_new_step')

    @patch.object(QuestionnaireSection, 'get_details')
    @patch('questionnaire.views.render')
    def test_calls_render(self, mock_render, mock_get_details):
        mock_get_details.return_value = "foo"
        generic_questionnaire_new(
            self.request, *get_valid_new_values()[0],
            **get_valid_new_values()[1])
        mock_render.assert_called_once_with(
            self.request, 'sample/questionnaire/details.html', {
                'questionnaire_id': None,
                'sections': ["foo"]*get_section_count(),
                'images': [],
                'mode': 'edit',
                'links': [],
            })

    def test_returns_rendered_response(self):
        ret = generic_questionnaire_new(
            self.request, *get_valid_new_values()[0],
            **get_valid_new_values()[1])
        self.assertIsInstance(ret, HttpResponse)


class GenericQuestionnaireDetailsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(reverse(
            route_questionnaire_details, args=[1]))

    @patch('questionnaire.views.get_object_or_404')
    def test_calls_get_object_or_404(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value.data = {}
        generic_questionnaire_details(
            self.request, *get_valid_details_values())
        mock_get_object_or_404.assert_called_once_with(Questionnaire, pk=1)

    @patch.object(QuestionnaireConfiguration, '__init__')
    @patch('questionnaire.views.get_object_or_404')
    @patch.object(QuestionnaireConfiguration, 'get_details')
    def test_creates_questionnaire_configuration(
            self, mock_QuestionnaireConfiguration_get_details,
            mock_get_object_or_404, mock_QuestionnaireConfiguration):
        mock_QuestionnaireConfiguration.return_value = None
        mock_get_object_or_404.return_value.data = {}
        # with self.assertRaises(Exception):
        generic_questionnaire_details(
            self.request, *get_valid_details_values())
        mock_QuestionnaireConfiguration.assert_called_once_with('sample')

    @patch.object(QuestionnaireConfiguration, 'get_details')
    @patch('questionnaire.views.get_object_or_404')
    def test_calls_get_details(self, mock_get_object_or_404, mock_get_details):
        mock_get_object_or_404.return_value.data = {}
        generic_questionnaire_details(
            self.request, *get_valid_details_values())
        mock_get_details.assert_called_once_with(
            data={}, questionnaire_object=mock_get_object_or_404.return_value)

    @patch.object(QuestionnaireConfiguration, 'get_image_data')
    @patch('questionnaire.views.get_object_or_404')
    def test_calls_get_image_data(
            self, mock_get_object_or_404, mock_get_image_data):
        mock_get_object_or_404.return_value.data = {}
        generic_questionnaire_details(
            self.request, *get_valid_details_values())
        mock_get_image_data.assert_called_once_with({})

    @patch('questionnaire.views.get_link_data')
    @patch('questionnaire.views.get_object_or_404')
    def test_calls_get_link_data(
            self, mock_get_object_or_404, mock_get_link_data):
        mock_get_object_or_404.return_value.data = {}
        generic_questionnaire_details(
            self.request, *get_valid_details_values())
        mock_get_link_data.assert_called_once_with(
            mock_get_object_or_404().links.all())

    @patch.object(QuestionnaireCategory, 'get_details')
    @patch('questionnaire.views.get_object_or_404')
    @patch('questionnaire.views.render')
    def test_calls_render(
            self, mock_render, mock_get_object_or_404, mock_get_details):
        mock_get_details.return_value = "foo"
        mock_get_object_or_404.return_value.data = {}
        generic_questionnaire_details(
            self.request, *get_valid_details_values())
        mock_render.assert_called_once_with(
            self.request, 'sample/questionnaire/details.html', {
                'sections': [],
                'questionnaire_id': 1,
                'mode': 'view',
                'images': [],
                'links': [],
            })

    @patch('questionnaire.views.get_object_or_404')
    def test_returns_rendered_response(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value.data = {}
        ret = generic_questionnaire_details(
            self.request, *get_valid_details_values())
        self.assertIsInstance(ret, HttpResponse)


@patch('questionnaire.views.advanced_search')
class GenericQuestionnaireListTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(reverse(route_questionnaire_list))

    @patch.object(QuestionnaireConfiguration, '__init__')
    @patch.object(QuestionnaireConfiguration, 'get_list_data')
    @patch.object(QuestionnaireConfiguration, 'get_filter_configuration')
    def test_creates_questionnaire_configuration(
            self, mock_Q_get_filter_configuration,
            mock_QuestionnaireConfiguration_get_list_data,
            mock_QuestionnaireConfiguration, mock_advanced_search):
        mock_QuestionnaireConfiguration.return_value = None
        generic_questionnaire_list(self.request, *get_valid_list_values())
        mock_QuestionnaireConfiguration.assert_called_once_with('sample')

    @patch('questionnaire.views.get_active_filters')
    @patch('questionnaire.views.QuestionnaireConfiguration')
    def test_calls_get_active_filters(
            self, mock_QuestionnaireConfiguration, mock_get_active_filters,
            mock_advanced_search):
        generic_questionnaire_list(self.request, *get_valid_list_values())
        mock_get_active_filters.assert_called_once_with(
            mock_QuestionnaireConfiguration.return_value, self.request.GET)

    @patch('questionnaire.views.get_configuration_index_filter')
    def test_calls_get_configuration_index_filter(
            self, mock_get_configuration_index_filter, mock_advanced_search):
        generic_questionnaire_list(self.request, *get_valid_list_values())
        mock_get_configuration_index_filter.assert_called_once_with(
            'sample', only_current=False)

    def test_calls_advanced_search(self, mock_advanced_search):
        generic_questionnaire_list(self.request, *get_valid_list_values())
        mock_advanced_search.assert_called_once_with(
            filter_params=[], query_string='', configuration_codes=['sample'],
            limit=10)

    @patch('questionnaire.views.get_list_values')
    def test_calls_get_list_values(
            self, mock_get_list_values, mock_advanced_search):
        generic_questionnaire_list(self.request, *get_valid_list_values())
        self.assertEqual(mock_get_list_values.call_count, 1)

    @patch.object(QuestionnaireConfiguration, 'get_filter_configuration')
    def test_calls_get_filter_configuration(
            self, mock_get_filter_configuration, mock_advanced_search):
        generic_questionnaire_list(self.request, *get_valid_list_values())
        mock_get_filter_configuration.assert_called_once_with()

    @patch('questionnaire.views.render')
    def test_calls_render(
            self, mock_render, mock_advanced_search):
        mock_advanced_search.return_value = {}
        generic_questionnaire_list(self.request, *get_valid_list_values())
        mock_render.assert_called_once_with(
            self.request, 'sample/questionnaire/list.html', {
                'list_values': [],
                'filter_configuration': (),
                'filter_url': '',
                'active_filters': [],
            })

    def test_returns_rendered_response(self, mock_advanced_search):
        ret = generic_questionnaire_list(
            self.request, *get_valid_list_values())
        self.assertIsInstance(ret, HttpResponse)

    def test_returns_only_template_values_if_no_template(
            self, mock_advanced_search):
        ret = generic_questionnaire_list(self.request, 'sample', template=None)
        self.assertIsInstance(ret, dict)


class GenericFileUploadTest(TestCase):

    fixtures = ['groups_permissions.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(file_upload_route)
        self.request = self.factory.post(self.url)
        self.request.user = create_new_user()

    def test_upload_login_required(self):
        self.client.logout()
        res = self.client.post(self.url, follow=True)
        self.assertTemplateUsed(res, 'login.html')

    def test_upload_only_post_allowed(self):
        res = generic_file_upload(self.request)
        self.assertEqual(res.status_code, 400)

    def test_handles_post_without_files(self):
        res = generic_file_upload(self.request)
        self.assertEqual(res.status_code, 400)
        content = json.loads(res.content.decode('utf-8'))
        self.assertFalse(content.get('success'))

    @patch('questionnaire.views.handle_upload')
    def test_calls_handle_upload(self, mock_handle_upload):
        m = Mock()
        m.get_url.return_value = 'foo'
        mock_handle_upload.return_value = m
        generic_file_upload(self.request)
        mock_handle_upload.assert_called_once()

    def test_handles_exception_by_handle_upload(self):
        res = generic_file_upload(self.request)
        self.assertEqual(res.status_code, 400)
        content = json.loads(res.content.decode('utf-8'))
        self.assertFalse(content.get('success'))


class GenericFileServeTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.file = File.create_new('image/jpeg')
        self.url = reverse(
            file_display_route, args=('display', self.file.uuid))
        self.request = self.factory.get(self.url)

    def test_raises_404_if_invalid_action(self):
        url = reverse(file_display_route, args=('foo', 'uid'))
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_raises_404_if_file_not_found(self):
        url = reverse(file_display_route, args=('display', 'uid'))
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    @patch('questionnaire.views.retrieve_file')
    def test_calls_retrieve_file(self, mock_retrieve_file):
        self.client.get(self.url)
        mock_retrieve_file.assert_called_once_with(self.file, thumbnail=None)

    @patch('questionnaire.views.retrieve_file')
    def test_calls_retrieve_file_with_thumbnail(self, mock_retrieve_file):
        self.client.get(self.url + '?format=foo')
        mock_retrieve_file.assert_called_once_with(self.file, thumbnail='foo')

    @patch('questionnaire.views.retrieve_file')
    def test_returns_file(self, mock_retrieve_file):
        mock_retrieve_file.return_value = ('file', 'filename')
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)

    @patch('questionnaire.views.retrieve_file')
    def test_returns_file_download(self, mock_retrieve_file):
        url = reverse(file_display_route, args=('download', self.file.uuid))
        mock_retrieve_file.return_value = ('file', 'filename')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
