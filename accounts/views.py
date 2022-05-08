from django.http import HttpResponse
from django.shortcuts import redirect, render
from accounts.models import Customer, Order, Service
from django.contrib import messages

# Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Generic views
from django.views.generic import CreateView


@login_required(login_url="login")
def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()[0:5]
    total_customers = customers.count()
    total_orders = orders.count()
    payed_orders = Order.objects.filter(payment_status="Done").count()
    context = {
        "customers": customers,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "payed_orders": payed_orders,
        "orders": orders,
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="login")
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer_orders = Order.objects.filter(customer_id=customer)
    context = {"customer": customer, "customer_orders": customer_orders}
    return render(request, "customer.html", context)


@login_required(login_url="login")
def customer_create(request):
    print(request)
    if request.method == "POST":
        customer = Customer(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
        )
        customer.save()
        return redirect("/")
    return render(request, "customer_create.html")
