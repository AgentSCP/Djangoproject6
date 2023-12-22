from django.shortcuts import render
from .models import Company, Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'product': products})

def create(request):
    companies = Company.objects.all()
    return render(request, 'create.html', context=)