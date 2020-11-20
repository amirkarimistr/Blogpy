from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class AllArticleApiView(APIView):

    def get(self, request):
        try:
            all_article = Article.objects.all().order_by('-created_at')[:9]
            data = []

            for article in all_article:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover.url else None,
                    'content': article.content,
                    'created_at': article.created_at,
                    'category': article.category.title,
                    'author': article.author.user.first_name+ ' '+ article.author.user.last_name,
                    'promote': article.promote
                })

            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': 'Internal server error'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
