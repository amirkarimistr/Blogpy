from django.urls import path
from .views import IndexPage as Index
from .views import ContactPage as Contact
from .views import AllArticleApiView as AllArticle
from .views import SingleArticleApiView as SingleArticle
from .views import SearchArticleApiView as SearchArticle
from .views import SubmitArticleApiView as SubmitArticle


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('article/all/', AllArticle.as_view(), name='all_articles'),
    path('article/', SingleArticle.as_view(), name='single_article'),
    path('article/search/', SearchArticle.as_view(), name='search_article'),
    path('article/submit/', SubmitArticle.as_view(), name='submit_article'),
]