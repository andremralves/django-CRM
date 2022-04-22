from django.urls import path
from . import views  # import functions from views

app_name = 'accounts'
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]
