from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden

def index(request):
    return render(request, 'breadcrumbs.html')

def link1(request):
    return render(request, 'link1.html')

def link2(request):
    return render(request, 'link2.html')

def link3(request):
    return render(request, 'link3.html')
