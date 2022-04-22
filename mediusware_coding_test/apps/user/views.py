from django.contrib.auth import views as views_auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"
    extra_context = {"page_title": _("PROFILE")}

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AuthLoginView(views_auth.LoginView):
    template_name = "base/login.html"
    redirect_authenticated_user = True


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _(
                "Your password was successfully updated"))
            return redirect("change-password")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request,
        "auth/change_password.html",
        {"form": form, "page_title": _("Change Password").upper()},
    )
