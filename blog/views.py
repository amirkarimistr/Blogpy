from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        all_articles = Article.objects.all()[:9]

        context = {
            'article_data': all_articles
        }

        return render(request, 'blog/index.html', context)
