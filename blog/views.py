from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        all_articles = Article.objects.all()[:9]
        all_promote_articles = Article.objects.filter(promote=True)

        context = {
            'article_data': all_articles,
            'promote_article_data': all_promote_articles
        }

        return render(request, 'blog/index.html', context)


class ContactPage(TemplateView):
    template_name = 'blog/page-contact.html'
