from django.http import JsonResponse
from products.models import Product


def api_home(request, *args, **kwargs):
    Product("title","content",100.00).save()
    data = Product.objects.all().order_by().first
    print(data)
    return JsonResponse(data)
