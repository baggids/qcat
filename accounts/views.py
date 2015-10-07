from django.contrib.auth import (
    logout as django_logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from qcat.utils import url_with_querystring
from accounts.authentication import (
    get_login_url,
    get_logout_url,
    get_session_cookie_name,
    get_user_information,
)
from accounts.models import User
from questionnaire.views import generic_questionnaire_list_no_config


def welcome(request):
    """
    The landing page of a user after he logged in. Update the user
    details and redirect to the page provided or "home".

    Args:
        ``request`` (django.http.HttpRequest): The request object.

    Returns:
        ``HttpResponse``. A rendered Http Response (through redirect)
    """
    home = reverse('home')
    redirect = request.GET.get('next', home)

    # In case the user was not logged in properly route him to "home"
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    session_id = request.COOKIES.get(get_session_cookie_name())
    if session_id is None:
        return HttpResponseRedirect(reverse('home'))

    # Update the user information
    user = request.user
    user_info = get_user_information(session_id, user.id)
    if user_info:
        user.update(
            lastname=user_info.get('last_name'),
            firstname=user_info.get('first_name'))

    messages.info(
        request, 'Welcome {}'.format(user_info.get('first_name')))

    return HttpResponseRedirect(redirect)


def login(request):
    """
    Show the login form or log in and redirect if the user is already
    authenticated. The actual authentication is handled by the
    authentication backend as specified in the settings (
    ``settings.AUTH_LOGIN_FORM``).

    .. seealso::
        :func:`accounts.authentication.get_login_url`

    After login, the user is sent to the welcome page where he is logged
    in in Django. Afterwards, he is redirected to the provided page
    (``next``) or to "home".

    * If the user is already logged in by Django: Redirect to the
      provided URL or to "home".

    * If the user is not logged in by Django and has no Session ID set,
      the login form is shown.

    Args:
        ``request`` (django.http.HttpRequest): The request object.

    Returns:
        ``HttpResponse``. A rendered Http Response.
    """
    redirect = request.GET.get('next', reverse('home'))

    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect)

    # Prevent that the URL is already encoded by inserting it afterwards
    welcome_url = url_with_querystring(
        reverse('welcome'), next='REDIRECT_URL')
    welcome_url = welcome_url.replace('REDIRECT_URL', redirect)

    return render(
        request, 'login.html', {
            'redirect_url': request.build_absolute_uri(welcome_url),
            'login_url': get_login_url(),
            'show_notice': redirect != reverse('home')
        })


def logout(request):
    """
    Log the user out. The actual logout is handled by the authentication
    backend as specified in the settings (``settings.AUTH_LOGIN_FORM``).

    Args:
        ``request`` (django.http.HttpRequest): The request object.

    Returns:
        ``HttpResponse``. A rendered Http Response.
    """
    redirect = reverse('home')

    django_logout(request)

    ses_id = request.COOKIES.get(get_session_cookie_name())
    if ses_id is not None:
        return HttpResponseRedirect(
            get_logout_url(request.build_absolute_uri(redirect)))

    return HttpResponseRedirect(redirect)


def questionnaires(request, user_id):
    """
    View to show the Questionnaires of a user.

    Args:
        ``request`` (django.http.HttpRequest): The request object.

    Returns:
        ``HttpResponse``. A rendered Http Response.
    """
    user = get_object_or_404(User, pk=user_id)

    list_template_values = generic_questionnaire_list_no_config(
        request, user=user)

    return render(request, 'questionnaires.html', list_template_values)


@login_required
def moderation(request):
    """
    View to show only pending Questionnaires to a moderator. Moderation
    permission (``can_moderate``) is needed for this view.

    Args:
        ``request`` (django.http.HttpRequest): The request object.

    Returns:
        ``HttpResponse``. A rendered Http Response.
    """
    if request.user.has_perm('questionnaire.can_moderate') is False:
        raise PermissionDenied()

    list_template_values = generic_questionnaire_list_no_config(
        request, moderation=True)

    return render(request, 'questionnaires.html', list_template_values)
