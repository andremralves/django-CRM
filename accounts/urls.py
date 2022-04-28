from django.urls import path
from . import views  # import functions from views

app_name = 'accounts'
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('cliente/<int:pk>', views.customer, name="customer"),
    path('cliente/create', views.customer_create, name="customer_create"),
]
