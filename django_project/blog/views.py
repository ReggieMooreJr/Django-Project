from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')
def search(request):
    return render(request, 'blog/search.html')
def cect(request):
    return render(request, 'blog/cect.html')


