from django.shortcuts import render
from accounts.models import Customer, Order
from django.shortcuts import redirect

# Auth
from django.contrib.auth.decorators import login_required


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
