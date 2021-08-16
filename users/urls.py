from django.contrib import admin
from django.urls import path,include

from customer.views import (
    NewCustomerFormView,
    CustomerListView,
    CustomerDetailView,
    CustomerUpdateView,
    CustomerDeleteView,
    RegisterFormView
    )
from customer import views

urlpatterns = [
    path('', CustomerListView.as_view(), name='index'),
    path('detail/<pk>', CustomerDetailView.as_view(), name="customer-detail"),
    path('update/<pk>', CustomerUpdateView.as_view(), name="customer-update"),
    path('delete/<pk>', CustomerDeleteView.as_view(), name='customer-delete'),
    path('new-customer/', NewCustomerFormView.as_view(), name="new-customer"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterFormView.as_view(), name="register"),
    path('admin/', admin.site.urls),
]