from django.shortcuts import render

from . import models
# Create your views here.
def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'product/products.html', {'products': products})