from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data_temp = serializer.data
        return Response(data_temp) 
    else:
        return Response({"error":"data is not valid",},status=500)