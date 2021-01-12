import pytest
from django.test import TestCase, RequestFactory, Client
from myapi.models import Customer, Order
from django.utils import timezone

from ..views import CustomerViewSet, OrderViewSet
from ..serializers import OrderSerializer

import json
from rest_framework.request import Request
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_204_NO_CONTENT)
from rest_framework.test import APIRequestFactory

# initialize the APIClient app
client = Client()

# Create your tests here.
"""TEST MODELS"""


class CustomerTest(TestCase):
    def create_customer(self, name="Kathurima", code="A01", phone_number="+254705385894"):
        return Customer.objects.create(name=name, code=code, phone_number=phone_number)

    def test_customer_creation(self):
        """Test Customer Creation"""
        customer = self.create_customer()
        self.assertTrue(isinstance(customer, Customer))
        self.assertTrue(customer.__str__(), customer.name)


class OrderTest(TestCase):
    def create_order(self, item="IPhone", amount=10, time=timezone.now()):
        return Order.objects.create(item=item, amount=amount, time=time)

    def test_order_creation(self):
        """Test Order Creation"""
        order = self.create_order()
        self.assertTrue(isinstance(order, Order))
        self.assertTrue(order.__str__(), order.item)


"""TESTING VIEWSETS"""


class CustomerViewSetTest(TestCase):
    def create_customer(self, name="Kathurima", code="A01", phone_number="+254705385894"):
        return Customer.objects.create(name=name, code=code, phone_number=phone_number)

    def test_customer_viewset(self):
        """Test Customer Viewset"""
        request = APIRequestFactory().get("")
        view = CustomerViewSet.as_view(actions={'get': 'list'})
        customer = self.create_customer()
        response = view(request, customer)
        self.assertEqual(response.status_code, 200)


class OrderViewSetTest(TestCase):
    def create_order(self, item="IPhone", amount=10, time=timezone.now()):
        return Order.objects.create(item=item, amount=amount, time=time)

    def test_order_viewset(self):
        """Test Order Viewset"""
        request = APIRequestFactory().get("")
        view = OrderViewSet.as_view(actions={'get': 'list'})
        order = self.create_order()
        response = view(request, order)
        self.assertEqual(response.status_code, 200)


"""TESTING SERIALIZER"""


@pytest.mark.django_db
class OrderSerializerTest(TestCase):
    def create_order(self, item="IPhone", amount=10, time=timezone.now()):
        return Order.objects.create(item=item, amount=amount, time=time)

    def test_order_serializer_create(self):
        request = APIRequestFactory().get("")
        context = {'request': Request(request)}
        order = self.create_order()
        order_serializer = OrderSerializer(order, context=context)

        data = {
            'item': order_serializer.data['item'],
            'amount': order_serializer.data['amount'],
            'time': order_serializer.data['time']
        }

        response = client.post(reverse('order-list'),
                               data=json.dumps(data),
                               content_type='application/json')

        assert response.status_code == HTTP_201_CREATED
