from django.urls import path
from .views import IndexPage as Index
from .views import ContactPage as Contact
from .views import AllArticleApiView as AllArticle

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('article/all/', AllArticle.as_view(), name='all_articles'),
]