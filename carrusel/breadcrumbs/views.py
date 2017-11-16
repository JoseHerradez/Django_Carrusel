import dominate
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from dominate.tags import *

from breadcrumbs.forms import ContentForm, BreadcrumbsForm
from breadcrumbs.models import BreadcrumbsContent, BreadcrumbsLevels


def index(request):
    return render(request, 'index.html')

def new_breadcrumbs(request):
    # bc = BreadcrumbsContent.objects.all()
    # print(bc)

    if request.method == "POST":
        form = BreadcrumbsForm(request.POST)
        if form.is_valid():
            breadcrumb = form.save()
            return redirect('breadcrumbs-patron:new_content', breadcrumb.id)
    else:
        form = BreadcrumbsForm()
    return render(request, 'new_breadcrumb.html', {'form': form})

def new_content(request, pk):
    breadcrumb = get_object_or_404(BreadcrumbsLevels, id=pk)
    count = range(breadcrumb.niveles)
    if request.method == "POST":
        forms = []
        for i in count:
            forms.append(ContentForm(request.POST, request.FILES, prefix=i))
        for form in forms:
            if form.is_valid():
                content = form.save(commit=False)
                print(content)
                content.breadcrumb = breadcrumb
                content.save()
            else:
                print("invalid")
                redirect('breadcrumbs_content')
        return redirect('breadcrumbs-patron:generar', breadcrumb.id)
        #return render(request,'breadcrumbs.html')
    else:
        forms = []
        for i in count:
            forms.append(ContentForm(prefix=i))
    return render(request, 'new_bc_content.html', {'forms': forms, 'pk':pk})

def generar(request, pk):
    breadcrumbs = get_object_or_404(BreadcrumbsContent, id=pk)
    bc = BreadcrumbsContent.objects.all()
    print(bc)
    elements = BreadcrumbsContent.objects.filter(breadcrumb=pk).values()
    data = {
        'title': breadcrumbs.title,
      	'url': breadcrumbs.url,
        'elements': elements
    }
    html = armarBreadcrumbsHTML(data)
    with open('patron/templates/breadcrumbs.html', 'w') as f:
        f.write("{% load static %}\n" + html["file"].render())        
    return render(request, 'breadcrumbs.html', {'htmlCode': html["code"].render()})
    
    
def armarBreadcrumbsHTML(data):
    if data is None:
        return None
    last = data['elements'].last()

    doc = dominate.document(title='Breadcrumbs') # el que se ve
    doc2 = dominate.document(title='Breadcrumbs') # el codigo de la caja

    with doc.head:
        link(href='https://fonts.googleapis.com/css?family=Alegreya+Sans:300,400|Source+Sans+Pro:400,300', rel='stylesheet', type='text/css')
        link(href="https://fonts.googleapis.com/icon?family=Material+Icons", rel="stylesheet")
        link(rel='stylesheet', href="{% static 'slick/slick.css' %}", type="text/css")
        link(rel='stylesheet', href="{% static 'slick/slick-theme.css' %}", type="text/css")
        link(rel='stylesheet', href="{% static 'prism/prism.css' %}", type="text/css")
        link(rel='stylesheet', href="{% static 'patron/style.css' %}", type="text/css")

    with doc:
        with nav(cls="breadcrumb"):
            for e in data['elements']:
                if e != last:
                    a(e['title'], cls="breadcrumb-item", href=e['url'])
                else:
                    span(e['title'], cls="breadcrumb-item active")
        br()
        h3("Para lograr este breadcrumbs en su página web, sólo copie el siguiente código:", style="text-align: center;")
        div(pre(code('{{ htmlCode }}', cls="language-html"), cls="language-html code-toolbar"), cls="code")
        script(type="text/javascript", src="//code.jquery.com/jquery-1.11.0.min.js")
        script(type="text/javascript", src="//code.jquery.com/jquery-migrate-1.2.1.min.js")
        script(type="text/javascript", src="{% static 'slick/slick.min.js' %}")
        script(type="text/javascript", src="{% static 'prism/prism.js' %}")
        script(type="text/javascript", src="{% static 'patron/script.js' %}")

    with doc2:
        with nav(cls="breadcrumb"):
            for e in data['elements']:
                if e != last:
                    a(e['title'], cls="breadcrumb-item", href=e['url'])
                else:
                    span(e['title'], cls="breadcrumb-item active")


    return { 'file': doc, 'code': doc2 }

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
