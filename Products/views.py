from rest_framework import permissions, viewsets

from .models import Products
from .serializer import ProductsSerializer


class ProductsView(viewsets.ModelViewSet):

    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
