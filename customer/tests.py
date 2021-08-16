from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from customer.models import Customer
from customer.forms import CustomerForm

class CustomerFieldTest(TestCase):

    def setUp(self):
        self.customer = Customer(tc_no='12345678911', name='Kaan', surname='Yavaş', 
        phone='12345678911', city='İzmir', state='Bornova')

    def test_field_tc(self):
        field_label = self.customer._meta.get_field('tc_no').verbose_name

        self.assertEqual(field_label, "tc no")

    def test_field_name(self):
        field_label = self.customer._meta.get_field('name').verbose_name

        self.assertEqual(field_label, "name")
    
    def test_field_surname(self):
        field_label = self.customer._meta.get_field('surname').verbose_name

        self.assertEqual(field_label, "surname")
    
    def test_object_name(self):
        expected_object = f'{self.customer.name}, {self.customer.surname}'
        self.assertEqual(str(self.customer), expected_object)


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class NewCustomerPageTest(TestCase):
    def test_new_customer_page_status_code(self):
        response = self.client.get('/new-customer/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('new-customer'))
        self.assertEqual(response.status_code, 200)
    
    def test_correct_template(self):
        response = self.client.get(reverse('new-customer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "new_customer.html")


class DetailCustomerPageTest(TestCase):
    
    def setUp(self):
        self.customer= Customer.objects.create(tc_no='12345678911', name='Kaan', surname='Yavaş', 
        phone='12345678911', city='İzmir', state='Bornova')

    def test_home_page_url_name(self):
        response = self.client.get(reverse('customer-detail', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_correct_template(self):
        response = self.client.get(reverse('customer-detail', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "customer_detail.html")

class UpdateCustomerPageTest(TestCase):
    
    def setUp(self):
        self.customer= Customer.objects.create(tc_no='12345678911', name='Kaan', surname='Yavaş', 
        phone='12345678911', city='İzmir', state='Bornova')

    def test_home_page_url_name(self):
        response = self.client.get(reverse('customer-update', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_correct_template(self):
        response = self.client.get(reverse('customer-update', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "customer_form_update.html")


class NewCustomerFormTest(TestCase):
    
    def test_valid_data(self):
        data = {'tc_no': '12345678997', 'name': 'Kaan', 'surname': 'Yavaş',
         'phone': '12345678911', 'city': 'İzmir', 'state': 'Bornova'}
        form = CustomerForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_blank_data(self):
        form = CustomerForm({'name': 'Kaan', 'surname': 'Yavaş',
         'phone': '12345', 'city': 'İzmir', 'state': 'Bornova'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'tc_no': ['This field is required.']})

    def test_form_error(self):
        form = CustomerForm({'tc_no': '12345', 'name': 'Kaan', 'surname': 'Yavaş',
         'phone': '12345', 'city': 'İzmir', 'state': 'Bornova'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'__all__': ['Check Your Information!']})


class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='1234test', email='test@test.com')

    def test_login(self):
        self.client.login(username='test', password='1234test')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response)
