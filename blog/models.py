from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  content = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)
  article = models.ForeignKey(Article)
  poster = models.CharField(max_length=32)

  def __str__(self):
    return self.content