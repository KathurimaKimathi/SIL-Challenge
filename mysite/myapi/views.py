from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status, viewsets

from .serializers import CustomerSerializer, OrderSerializer
from .models import Customer, Order


# Create your views here.
# @method_decorator(login_required, name='dispatch')
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('code')
    serializer_class = CustomerSerializer


# @method_decorator(login_required, name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('time')
    serializer_class = OrderSerializer
