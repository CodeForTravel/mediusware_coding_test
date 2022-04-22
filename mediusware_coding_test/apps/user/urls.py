from django.urls import path
from mediusware_coding_test.apps.user import views as views_user

app_name = "user"

urlpatterns = [
    path("profile/", views_user.UserProfileView.as_view(), name="profile"),
]
