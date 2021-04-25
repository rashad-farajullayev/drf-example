from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

import Customers.views
from Customers.models import Customer


class TestCustomer(TestCase):
    def setUp(self):
        Customer.objects.create(first_name="Rashad", last_name="Farajullayev", email="rashadex@gmail.com", birth_date=datetime.today())
        Customer.objects.create(first_name="John", last_name="Doe", email="john.doe@microsoft.com", birth_date=datetime.today())
        User.objects.create_user(username='admin', password='admin', email='rashadex@gmail.com')

    def test_get_all_customers(self):
        """
            Ensure we can list all customers
        """
        factory = APIRequestFactory()
        request = factory.get('customers/')
        view = Customers.views.CustomersView.as_view({'get': 'list'})
        user = User.objects.get(username='admin')
        force_authenticate(request, user=user)
        response = view(request)
        response.render()
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['first_name'], 'Rashad')
        self.assertEqual(response.data['results'][0]['last_name'], 'Farajullayev')
