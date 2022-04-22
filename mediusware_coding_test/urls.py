"""mediusware_coding_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mediusware_coding_test.apps.user import views as views_user


urlpatterns = [
    path("admin/", admin.site.urls),

    # path("change-password/", views_user.change_password, name="change-password"),
    path("logout/", LogoutView.as_view(), name="user-logout"),
    # path("account/", include("django.contrib.auth.urls")),
    # django urls
    path("", include("mediusware_coding_test.core.urls")),

    # path("user/", include("mediusware_coding_test.apps.user.urls")),
    # REST API ENDPOINTS
    path(
        r"api/v1/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("api/v1/user/", include("mediusware_coding_test.apps.user.api.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
