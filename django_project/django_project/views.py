import django.http


def index(request):
    return django.http.HttpResponse("Hello My Friends")


def miko(request):
    return django.http.HttpResponse("This page will be used to show Mikos information")


def milani(request):
    return django.http.HttpResponse("This will be the page for milani")


def searchpage(request):
    return django.http.HttpResponse("This is the Search Page for SDL")

def familymatters(request):
    return django.http.HttpResponse("This is a joke page")
