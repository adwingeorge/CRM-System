from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Customer

class AccountsTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='secret', email='test@example.com'
        )
        self.client.login(username='testuser', password='secret')
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            address="123 Main St",
            created_by=self.user
        )

    def test_customer_list_view(self):
        response = self.client.get(reverse('customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_customer_detail_view(self):
        response = self.client.get(reverse('customer_detail', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_create_customer_view(self):
        response = self.client.post(reverse('create_customer'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'phone_number': '0987654321',
            'address': '321 Main St',
            'email': 'jane.doe@example.com'  # Add email field
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation

    def test_update_customer_view(self):
        response = self.client.post(reverse('update_customer', args=[self.customer.id]), {
            'first_name': 'Johnny',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'address': '123 Main St',
            'email': 'johnny.doe@example.com'  # Add email field
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after update

    def test_delete_customer_view(self):
        response = self.client.post(reverse('delete_customer', args=[self.customer.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after deletion
        self.assertFalse(Customer.objects.filter(id=self.customer.id).exists())