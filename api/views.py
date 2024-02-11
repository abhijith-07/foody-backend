from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def products(request):
    if request.method == 'GET':
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)