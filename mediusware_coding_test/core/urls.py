from django.urls import path
from mediusware_coding_test.core import views as views_core
from mediusware_coding_test.apps.user import views as views_user

app_name = "core"

urlpatterns = [
    path("", views_core.HomeView.as_view(), name="home"),
    path("login", views_user.AuthLoginView.as_view(), name="login"),
    # visit records export urls
]


# urls for login, password reset
auth_template_url_paths = [
    ["login/", "login"],
    ["account/password_reset/", "password-reset"],
    ["account/password_reset/done/", "password-reset-done"],
    ["account/reset/done/", "password-reset-complete"],
    ["account/reset/<str:token>/confirm/", "password-reset-confirm"],
]
for path__ in auth_template_url_paths:
    urlpatterns.append(
        path(path__[0], views_core.IndexView.as_view(), name=path__[1]))


# urls for sys-admin dashboard app
sysadmin_dashboard_url_paths = [
    # first index is path, second index is name
    ["user/profile/", "profile"],
    ["dashboard/", "dashboard"],
    ["settings/syadmin/general/", "sysadmin-general-settings"],
]
for path__ in sysadmin_dashboard_url_paths:
    urlpatterns.append(
        path(path__[0], views_core.SysadminIndexView.as_view(), name=path__[1])
    )
