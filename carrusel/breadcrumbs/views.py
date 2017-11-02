from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden

def index(request):
    return render(request, 'breadcrumbs.html')

def link1(request):
    return render(request, 'link1.html')

def interno1(request):
    return render(request, 'interno1.html')

def interno2(request):
    return render(request, 'interno2.html')

def interno3(request):
    return render(request, 'interno3.html')

def link2(request):
    return render(request, 'link2.html')

def link3(request):
    return render(request, 'link3.html')
