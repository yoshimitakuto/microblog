from django.contrib import admin
from django.urls import path

from blog.views import toppage, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', toppage, name='toppage'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]
