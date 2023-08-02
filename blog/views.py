from django.shortcuts import render

def toppage(request):
    return render(request, 'blog/toppage.html')
