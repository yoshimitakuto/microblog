from django.contrib import admin
from django.urls import path

from blog.views import toppage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', toppage),
]
