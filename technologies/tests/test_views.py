from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from unittest.mock import patch, Mock

from accounts.tests.test_authentication import create_new_user
from qcat.tests import TestCase
from technologies.views import (
    questionnaire_details,
    questionnaire_link_form,
    questionnaire_link_search,
    questionnaire_list,
    questionnaire_list_partial,
    questionnaire_new,
    questionnaire_new_step,
)


route_home = 'technologies:home'
route_questionnaire_details = 'technologies:questionnaire_details'
route_questionnaire_link_form = 'technologies:questionnaire_link_form'
route_questionnaire_list = 'technologies:questionnaire_list'
route_questionnaire_list_partial = 'technologies:questionnaire_list_partial'
route_questionnaire_new = 'technologies:questionnaire_new'
route_questionnaire_new_step = 'technologies:questionnaire_new_step'


def get_valid_details_values():
    return (1, 'technologies', 'technologies/questionnaire/details.html')


def get_valid_link_form_values():
    args = ('technologies', 'technologies')
    kwargs = {'page_title': 'Technology Links'}
    return args, kwargs


def get_valid_new_values():
    args = (
        'technologies', 'technologies/questionnaire/details.html',
        'technologies')
    kwargs = {'questionnaire_id': None}
    return args, kwargs


def get_valid_new_step_values():
    args = (get_categories()[0][0], 'technologies', 'technologies')
    kwargs = {'page_title': 'Technologies Form'}
    return args, kwargs


def get_category_count():
    return len(get_categories())


def get_categories():
    return (
        ('tech__1', 'General Information'),
        ('tech__2', 'Specification of the SLM practice'),
        ('tech__2a', 'Land Use'),
    )


class HomeTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(route_home)

    @patch('questionnaire.views.advanced_search')
    def test_renders_correct_template(self, mock_advanced_search):
        res = self.client.get(self.url)
        self.assertTemplateUsed(res, 'technologies/questionnaire/list.html')
        self.assertEqual(res.status_code, 200)


class QuestionnaireLinkFormTest(TestCase):

    def setUp(self):
        self.url = reverse(route_questionnaire_link_form)

    def test_login_required(self):
        res = self.client.get(self.url, follow=True)
        self.assertTemplateUsed(res, 'login.html')

    @patch('technologies.views.generic_questionnaire_link_form')
    def test_calls_generic_function(self, mock_generic_function):
        request = Mock()
        questionnaire_link_form(request)
        mock_generic_function.assert_called_once_with(
            request, *get_valid_link_form_values()[0],
            **get_valid_link_form_values()[1])


class QuestionnaireLinkSearchTest(TestCase):

    @patch('technologies.views.generic_questionnaire_link_search')
    def test_calls_generic_function(self, mock_generic_function):
        request = Mock()
        questionnaire_link_search(request)
        mock_generic_function.assert_called_once_with(request, 'technologies')


class QuestionnaireNewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(route_questionnaire_new)

    def test_questionnaire_new_login_required(self):
        res = self.client.get(self.url, follow=True)
        self.assertTemplateUsed(res, 'login.html')

    def test_questionnaire_new_test_renders_correct_template(self):
        request = self.factory.get(self.url)
        request.user = create_new_user()
        res = questionnaire_new(request)
        self.assertTemplateUsed(res, 'technologies/questionnaire/details.html')
        self.assertEqual(res.status_code, 200)

    @patch('technologies.views.generic_questionnaire_new')
    def test_calls_generic_function(self, mock_questionnaire_new):
        request = self.factory.get(self.url)
        request.user = create_new_user()
        questionnaire_new(request)
        mock_questionnaire_new.assert_called_once_with(
            request, *get_valid_new_values()[0], **get_valid_new_values()[1])


class QuestionnaireNewStepTest(TestCase):

    fixtures = [
        'groups_permissions.json', 'global_key_values.json',
        'technologies.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(
            route_questionnaire_new_step, args=[get_categories()[0][0]])

    def test_questionnaire_new_step_login_required(self):
        res = self.client.get(self.url, follow=True)
        self.assertTemplateUsed(res, 'login.html')

    def test_renders_correct_template(self):
        request = self.factory.get(self.url)
        request.user = create_new_user()
        res = questionnaire_new_step(request, step=get_categories()[0][0])
        self.assertTemplateUsed(res, 'form/category.html')
        self.assertEqual(res.status_code, 200)

    @patch('technologies.views.generic_questionnaire_new_step')
    def test_calls_generic_function(self, mock_questionnaire_new_step):
        request = self.factory.get(self.url)
        request.user = create_new_user()
        questionnaire_new_step(request, get_categories()[0][0])
        mock_questionnaire_new_step.assert_called_once_with(
            request, *get_valid_new_step_values()[0],
            **get_valid_new_step_values()[1])


class QuestionnaireDetailsTest(TestCase):

    fixtures = [
        'groups_permissions.json', 'global_key_values.json',
        'technologies.json', 'technologies_questionnaires.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(route_questionnaire_details, args=[101])

    def test_renders_correct_template(self):
        res = self.client.get(self.url, follow=True)
        self.assertTemplateUsed(res, 'technologies/questionnaire/details.html')
        self.assertEqual(res.status_code, 200)

    @patch('technologies.views.generic_questionnaire_details')
    def test_calls_generic_function(self, mock_questionnaire_details):
        request = self.factory.get(self.url)
        questionnaire_details(request, 1)
        mock_questionnaire_details.assert_called_once_with(
            request, *get_valid_details_values())


class QuestionnaireListPartialTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(route_questionnaire_list_partial)

    @patch('technologies.views.generic_questionnaire_list')
    def test_calls_generic_questionnaire_list(self, mock_questionnaire_list):
        request = self.factory.get(self.url)
        questionnaire_list_partial(request)
        mock_questionnaire_list.assert_called_once_with(
            request, 'technologies', template=None)

    @patch('technologies.views.render_to_string')
    @patch('technologies.views.generic_questionnaire_list')
    def test_calls_render_to_string_with_list_template(
            self, mock_questionnaire_list, mock_render_to_string):
        mock_questionnaire_list.return_value = {
            'list_values': 'foo',
            'active_filters': 'bar'
        }
        mock_render_to_string.return_value = ''
        self.client.get(self.url)
        mock_render_to_string.assert_any_call(
            'technologies/questionnaire/partial/list.html',
            {'list_values': 'foo'})

    @patch('technologies.views.render_to_string')
    @patch('technologies.views.generic_questionnaire_list')
    def test_calls_render_to_string_with_active_filters(
            self, mock_questionnaire_list, mock_render_to_string):
        mock_questionnaire_list.return_value = {
            'list_values': 'foo',
            'active_filters': 'bar'
        }
        mock_render_to_string.return_value = ''
        self.client.get(self.url)
        mock_render_to_string.assert_any_call(
            'active_filters.html', {'active_filters': 'bar'})


class QuestionnaireListTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse(route_questionnaire_list)

    @patch('technologies.views.generic_questionnaire_list')
    def test_calls_generic_function(self, mock_generic_function):
        request = Mock()
        questionnaire_list(request)
        mock_generic_function.assert_called_once_with(
            request, 'technologies',
            template='technologies/questionnaire/list.html',
            filter_url=reverse(route_questionnaire_list_partial))