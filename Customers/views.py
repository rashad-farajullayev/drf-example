from rest_framework import permissions, viewsets

from .models import Customer
from .serializer import CustomerSerializer


class CustomersView(viewsets.ModelViewSet):

    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
