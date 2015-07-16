from django.shortcuts import render

from .models import Article, Comment

# Create your views here.
def blog_list(request):
  articles = Article.objects.all()
  return render(request, 'blog/blog_list.html', {
    'articles': articles
  })