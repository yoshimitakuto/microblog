from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
