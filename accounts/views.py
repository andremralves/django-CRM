from django.http import HttpResponse
from django.shortcuts import redirect, render
from accounts.models import Customer, Order, Service
from django.contrib import messages

# Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Generic views
from django.views.generic import CreateView

# Create your views here.

# Extends the Generic View
class LoginView(CreateView):
    template_name = "registration/login.html"

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)


@login_required(login_url="login")
def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()[0:5]
    total_customers = customers.count()
    total_orders = orders.count()
    context = {
        "customers": customers,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "orders": orders,
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="login")
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    print(customer)
    context = {"customer": customer}
    return render(request, "customer.html", context)


@login_required(login_url="login")
def customer_create(request):
    return render(request, "customer_create.html")
