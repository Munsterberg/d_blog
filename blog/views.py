from django.shortcuts import render, get_object_or_404

from .models import Article, Comment

# Create your views here.
def blog_list(request):
  articles = Article.objects.all()
  return render(request, 'blog/blog_list.html', {
    'articles': articles
  })

def blog_detail(request, pk):
  article = get_object_or_404(Article, pk=pk)
  return render(request, 'blog/blog_detail.html', {
    'article': article,
  })