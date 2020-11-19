from django.urls import path
from .views import IndexPage as Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]