from django.urls import path
from . import views  # import functions from views
from django.views.generic import TemplateView

# when calling urls in templates views u need to put name space
# app_name = "customers"
urlpatterns = [
    path("cliente/<int:pk>", views.customer, name="customer"),
    path("cliente/create", views.customer_create, name="customer_create"),
    path("clientes", views.customers, name="customers"),
]
