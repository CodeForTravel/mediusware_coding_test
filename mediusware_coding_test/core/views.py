from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse


class HomeView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect("admin:index")
            elif request.user.is_sysadmin:
                return redirect("core:dashboard")
            else:
                return redirect("core:profile")

        return super().dispatch(request, *args, **kwargs)


class IndexView(TemplateView, View):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_sysadmin:
                return redirect("core:dashboard")
        return super().dispatch(request, *args, **kwargs)


class SysadminIndexView(LoginRequiredMixin, TemplateView):
    template_name = "user/sys_admin/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not (request.user.is_sysadmin):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
