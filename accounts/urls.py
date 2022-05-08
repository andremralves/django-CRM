from django.urls import path
from . import views  # import functions from views
from django.views.generic import TemplateView

# when calling urls in templates views u need to put name space
# app_name = "accounts"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("cliente/<int:pk>", views.customer, name="customer"),
    path("cliente/create", views.customer_create, name="customer_create"),
    path("about/", TemplateView.as_view(template_name="customer_create.html")),
]
