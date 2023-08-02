from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
