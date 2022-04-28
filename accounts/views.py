from django.shortcuts import render

from accounts.models import Customer

# Create your views here.


def dashboard(request):
    customers = Customer.objects.all()
    print(customers)
    context = {'customers': customers}
    return render(request, 'accounts/dashboard.html', context)


def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    print(customers)
    context = {'customer': customer}
    return render(request, 'accounts/customer.html', context)


def customer_create(request):
    return render(request, 'accounts/customer_create.html')
