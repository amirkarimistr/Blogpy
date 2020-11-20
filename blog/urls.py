from django.urls import path
from .views import IndexPage as Index
from .views import ContactPage as Contact


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
]