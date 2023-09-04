from django.urls import re_path
from applications.authentication.views import LoginView

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view()),
]