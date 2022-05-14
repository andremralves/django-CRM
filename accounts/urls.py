from django.urls import path
from . import views  # import functions from views
from django.views.generic import TemplateView

# when calling urls in templates views u need to put name space
# app_name = "accounts"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
