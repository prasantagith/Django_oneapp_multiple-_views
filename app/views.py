from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def data1(requset):
    return HttpResponse("hii")

def data2(requset):
    return HttpResponse("hello")

def data3(requset):
    a=30
    b=40
    return HttpResponse (a+b)
def data4(requset):
    p="prasanta sethi"
    return HttpResponse(f'<h2>hello how are you  { p}</h2>')
    