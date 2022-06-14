from django.shortcuts import render, HttpResponse

def hello(request, nome):
    return HttpResponse('<h1>Hello {} !</h1>'.format(nome))


