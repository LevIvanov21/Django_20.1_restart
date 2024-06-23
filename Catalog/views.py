from django.shortcuts import render

from Catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'Catalog/base.html', context)


# def index(request):
#     return render(request, "catalog/home.html")
#
#
# def contacts(request):
#     return render(request, "catalog/contacts.html")
