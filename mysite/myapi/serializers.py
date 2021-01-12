from rest_framework import serializers

from .models import Customer, Order

import africastalking

from decouple import config


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'code', 'phone_number')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'item', 'amount', 'time')

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        sendsms()
        return order


# Sending SMS via Africa's Talking
def sendsms():
    # Initializing SDK
    username = config('AT_USERNAME')
    api_key = config('AT_API_KEY')
    africastalking.initialize(username, api_key)

    # Initializing SMS service
    sms = africastalking.SMS

    # Using service Synchronously
    response = sms.send("Dear Esteemed customer, new orders available. Kindly check them out.", ["+254705385894"])
    print(response)

    # Using the system Asynchronously
    # def on_finish(error, response):
    #    if error is not None:
    #        raise error
    #    print(response)

    # customer_contacts = Customer.objects.values_list('phone_number')
    # sms.send("Dear Esteemed customer, new orders available. Kindly check them out.", ['+254705385894'],
    #         callback=on_finish)
