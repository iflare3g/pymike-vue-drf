# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
#
# from .models import Product
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
from django.http import JsonResponse
from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values("pk", "name"))}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    status = 200
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.get_photo_url,
                "price": product.price,
                "shipping_price": product.shipping_price,
                "quantity": product.quantity,
            }
        }
    except Product.DoesNotExist:
        data = {"error": {"code": 404, "message": "Product not found!"}}
        status = 404
    return JsonResponse(data, status=status)


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    data = {"manufacturers": list(manufacturers.values("pk", "name"))}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    status = 200
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer.products.values("name")),
            }
        }
    except Manufacturer.DoesNotExist:
        data = {"error": {"code": 404, "message": "Manufacturer not found!"}}
        status = 404
    return JsonResponse(data, status=status)
