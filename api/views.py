from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()  # Set the queryset here
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # You can keep this permission class if needed
