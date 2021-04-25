from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .permissions import IsOwnerOfOrder
from .serializer import OrderSerializer, OrderDetailsSerializer


class OrderListView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfOrder]
    serializer_class = OrderDetailsSerializer

    def get(self, request, customer_id):

        self.check_permissions(request)

        orders = Order.objects.filter(customer_id=customer_id)
        for order in orders:
            self.check_object_permissions(request, order)

        serializer = OrderDetailsSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, customer_id):
        serializer = OrderDetailsSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.save():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            Response("Provided data does not appear to be valid", status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
