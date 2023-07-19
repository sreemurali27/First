from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string_response(request):
    return HttpResponse('this is my first string')
def second(request):
    return HttpResponse('Second response')
def third(request):
    return HttpResponse('Third one')
def fun(request):
    return HttpResponse('<h1><center>Vanakam da mapla Salem larundhu</center></h1>')