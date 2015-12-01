from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from unittest.mock import patch

from functional_tests.base import FunctionalTest
from accounts.models import User
from accounts.tests.test_models import create_new_user
from accounts.tests.test_views import accounts_route_moderation

from nose.plugins.attrib import attr
# @attr('foo')

@patch('accounts.authentication.auth_authenticate')
class LoginTest(FunctionalTest):

    def test_login(self, mock_authenticate):

        user = create_new_user()
        user.backend = 'django.contrib.auth.backends.ModelBackend'

        mock_authenticate.return_value = None

        # Alice opens her web browser and goes to the home page
        self.browser.get(self.live_server_url)

        # She sees the top naviation bar with the login button, on which she
        # clicks.
        navbar = self.findBy('class_name', 'top-bar')
        navbar.find_element_by_link_text('Login').click()

        # She tries to submit the form empty and sees that the form was
        # not submitted.
        self.findBy('id', 'button_login').click()
        self.findBy('name', 'user')

        # She enters some (wrong) user credentials
        self.findBy('name', 'user').send_keys('wrong@user.com')
        self.findBy('name', 'pass').send_keys('wrong')

        # She tries to submit the form and sees an error message
        self.findBy('id', 'button_login').click()

        self.checkOnPage('WOCAT login failure')
        # self.findBy('class_name', 'alert-box')
        # self.checkOnPage('not correct')

        mock_authenticate.return_value = user

        self.browser.get(self.live_server_url)
        self.browser.add_cookie({'name': 'fe_typo_user', 'value': 'foo'})
        self.browser.get(self.live_server_url)

        self.checkOnPage('Logout')

        # She submits the form and notices she is being redirected to the home
        # page and she is now logged in (the top bar showing a logout button).
        # self.assertEqual(self.browser.current_url, self.live_server_url + '/')
        # navbar = self.findBy('class_name', 'top-bar')
        # navbar.find_element_by_link_text('Logout')


@patch('accounts.authentication.auth_authenticate')
class UserTest(FunctionalTest):

    fixtures = ['groups_permissions.json']

    def test_superusers(self, mock_authenticate):
        user = create_new_user()
        user.is_superuser = True
        user.backend = 'accounts.authentication.WocatAuthenticationBackend'
        mock_authenticate.return_value = user
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie({'name': 'fe_typo_user', 'value': 'foo'})
        self.browser.get(self.live_server_url)

        # Superusers see the link to the administration
        self.findBy(
            'xpath', '//ul[@class="dropdown"]/li/a[@href="/admin/"]')

        # Superusers see the link to the Dashboard
        self.findBy(
            'xpath', '//ul[@class="dropdown"]/li/a[contains(@href, "search/'
            'admin")]')

    def test_administrators(self, mock_authenticate):
        user = create_new_user()
        user.groups = [Group.objects.get(pk=1)]
        user.backend = 'accounts.authentication.WocatAuthenticationBackend'
        mock_authenticate.return_value = user
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie({'name': 'fe_typo_user', 'value': 'foo'})
        self.browser.get(self.live_server_url)

        # Administrators see the link to the administration
        self.findBy(
            'xpath', '//ul[@class="dropdown"]/li/a[@href="/admin/"]')

        # Administrators do not see the link to the Dashboard
        self.findByNot(
            'xpath', '//ul[@class="dropdown"]/li/a[contains(@href, "search/'
            'admin")]')

    def test_moderators(self, mock_authenticate):
        user = create_new_user()
        user.groups = [Group.objects.get(pk=3)]
        user.backend = 'accounts.authentication.WocatAuthenticationBackend'
        mock_authenticate.return_value = user
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie({'name': 'fe_typo_user', 'value': 'foo'})
        self.browser.get(self.live_server_url)

        # Moderators do not see the link to the administration
        self.findByNot(
            'xpath', '//ul[@class="dropdown"]/li/a[@href="/admin/"]')

        # Moderators do not see the link to the Dashboard
        self.findByNot(
            'xpath', '//ul[@class="dropdown"]/li/a[contains(@href, "search/'
            'admin")]')

    def test_translators(self, mock_authenticate):
        user = create_new_user()
        user.groups = [Group.objects.get(pk=2)]
        user.backend = 'accounts.authentication.WocatAuthenticationBackend'
        mock_authenticate.return_value = user
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie({'name': 'fe_typo_user', 'value': 'foo'})
        self.browser.get(self.live_server_url)

        # Translators see the link to the administration
        self.findBy(
            'xpath', '//ul[@class="dropdown"]/li/a[@href="/admin/"]')

        # Translators do not see the link to the Dashboard
        self.findByNot(
            'xpath', '//ul[@class="dropdown"]/li/a[contains(@href, "search/'
            'admin")]')

# @patch('accounts.authentication.WocatAuthenticationBackend._do_auth')
# class LogoutTest(FunctionalTest):

#     def test_logout(self, mock_do_auth):

#         mock_do_auth.return_value = ('tempsessionid')

#         # Alice logs in
#         self.doLogin('a@b.com', 'foo')

#         # She sees a logout button in the top navigation bar and clicks on it
#         navbar = self.findBy('class_name', 'top-bar')
#         navbar.find_element_by_link_text('Logout').click()

#         # She notices she was redirected to the home page and is now logged
#         # out (the top bar showing a login button)
#         self.assertEqual(self.browser.current_url, self.live_server_url + '/')
#         navbar = self.findBy('class_name', 'top-bar')
#         navbar.find_element_by_link_text('Login')


class ModerationTest(FunctionalTest):

    fixtures = [
        'groups_permissions.json', 'global_key_values.json', 'sample.json',
        'sample_questionnaire_status.json', 'sample_user.json']

    """
    id: 1   code: sample_1   version: 1   status: 1   user: 101
    id: 2   code: sample_2   version: 1   status: 2   user: 102
    id: 3   code: sample_3   version: 1   status: 3   user: 101, 102
    id: 4   code: sample_4   version: 1   status: 4   user: 101
    id: 5   code: sample_5   version: 1   status: 5   user: 101
    id: 6   code: sample_5   version: 2   status: 3   user: 101
    id: 7   code: sample_6   version: 1   status: 1   user: 103
    """

    def test_user_questionnaires(self):

        user_alice = User.objects.get(pk=101)
        user_moderator = User.objects.get(pk=2365)

        # Alice logs in
        self.doLogin(user=user_alice)

        # She tries to access the moderation view but permission is denied
        self.browser.get(self.live_server_url + reverse(
            accounts_route_moderation))
        self.checkOnPage('403 Forbidden')

        # She logs in as moderator and sees that she can access the view
        self.doLogin(user=user_moderator)
        self.browser.get(self.live_server_url + reverse(
            accounts_route_moderation))

        # She sees all the Questionnaires which are pending.
        list_entries = self.findManyBy(
            'xpath', '//article[contains(@class, "tech-item")]')
        self.assertEqual(len(list_entries), 1)
        self.findBy(
            'xpath', '(//article[contains(@class, "tech-item")])[1]//h1/a['
            'contains(text(), "Foo 2")]')

        # She also sees a customized title of the list
        self.findByNot(
            'xpath', '//h2[contains(text(), "SLM practices by")]')
        self.findBy(
            'xpath', '//h2[contains(text(), "Pending SLM practices")]')
