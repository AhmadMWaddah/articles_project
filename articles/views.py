from django.shortcuts import render
from .models import Article, Account


def view_articles(request):
	account = request.user
	articles = Article.objects.all().filter(account=account)
	return render(request, 'articles/articles.html', {'articles': articles})


def article_details(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article': article})