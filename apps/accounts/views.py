from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    logout as django_logout,
    login as django_login,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_POST
from django.views.generic import FormView

from questionnaire.views import generic_questionnaire_list_no_config
from .authentication import (
    get_logout_url,
    search_users,
    update_user,
    get_user_information)
from .models import User


class LoginView(FormView):
    """
    This view handles the login form and authenticates users.
    """
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = 'home'

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # Put the user on the request, and add a welcome message.
        user = form.get_user()
        django_login(self.request, user)
        messages.info(self.request, 'Welcome {}'.format(user.firstname))

        # Get the response, add a cookie and return it.
        response = HttpResponseRedirect(reverse(self.get_success_url()))
        # We really should set a signed cookie - but the same cookie is used
        # on wocat.net.
        response.set_cookie(
            key=settings.AUTH_COOKIE_NAME,
            value=user.typo3_session_id
        )
        return response

    def get_success_url(self):
        # Explicitly passed ?next= url takes precedence.
        redirect_to = self.request.GET.get('next') or self.success_url
        # Prevent redirecting to other/invalid hosts - i.e. prevent xsrf
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
        return redirect_to


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

    ses_id = request.COOKIES.get(settings.AUTH_COOKIE_NAME)
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
    permission (``review_questionnaire``) is needed for this view.

    Args:
        ``request`` (django.http.HttpRequest): The request object.

    Returns:
        ``HttpResponse``. A rendered Http Response.
    """
    if request.user.has_perm('questionnaire.review_questionnaire') is False:
        raise PermissionDenied()

    list_template_values = generic_questionnaire_list_no_config(
        request, moderation_mode='review')

    return render(request, 'questionnaires.html', list_template_values)


def user_search(request):
    """
    JSON view to search for users. The search is handled by the
    authentication backend as specified in the settings
    (``settings.AUTH_LOGIN_FORM``).

    Args:
        ``request`` (django.http.HttpRequest): The request object with
        optional GET parameter ``name``.

    Returns:
        ``JsonResponse``. A rendered JSON response.
    """
    search = search_users(name=request.GET.get('name', ''))
    if not search:
        search = {
            'success': False,
            'message': 'Error: The user database cannot be queried right now.'
        }

    return JsonResponse(search)


@require_POST
@login_required
def user_update(request):
    """
    JSON view to create or update a user. The user is queried through
    the authentication backend as specified in the settings
    (``settings.AUTH_LOGIN_FORM``).

    Args:
        ``request`` (django.http.HttpRequest): The request object with
        POST parameter ``uid`` (the user ID).

    Returns:
        ``JsonResponse``. A rendered JSON response.
    """
    ret = {
        'success': False,
    }

    user_uid = request.POST.get('uid')
    if user_uid is None:
        ret['message'] = 'No user ID (uid) provided.'
        return JsonResponse(ret)

    # Try to find the user in the authentication DB
    user_info = get_user_information(user_uid)
    if not user_info:
        ret['message'] = 'No user with ID {} found in the authentication '
        'database.'.format(user_uid)
        return JsonResponse(ret)

    # Update (or insert) the user details in the local database
    user, created = User.objects.get_or_create(pk=user_uid)
    update_user(user, user_info)

    ret = {
        'name': user.get_display_name(),
        'success': True,
    }
    return JsonResponse(ret)


def details(request, id):
    """
    View for the details of a user. Also does an update of the user
    information against the authentication backend.

    Args:
        ``request`` (django.http.HttpRequest): The request object.

        ``id`` (int): The ID of the user.

    Returns:
        ``HttpResponse``. A rendered Http Response.
    """
    user = get_object_or_404(User, pk=id)

    # Update the user details
    user_info = get_user_information(user.id)
    update_user(user, user_info)

    return render(request, 'details.html', {
        'detail_user': user,
    })
