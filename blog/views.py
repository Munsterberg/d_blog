from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect

from .models import Article, Comment
from .forms import CommentForm

# Create your views here.
def blog_list(request):
  articles = Article.objects.all().order_by("-created_at")
  return render(request, 'blog/blog_list.html', {
    'articles': articles
  })

def blog_detail(request, pk):
  if request.method == 'POST':
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.article_id = pk
      comment.save()
      return HttpResponseRedirect('/blog/%s' % pk)
  else:
    form = CommentForm()      

  article = get_object_or_404(Article, pk=pk)
  comments = Comment.objects.filter(article_id=pk)
  return render(request, 'blog/blog_detail.html', {
    'article': article,
    'comments': comments,
    'form': form,
  })


        