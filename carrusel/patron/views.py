from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import *
from patron.forms import ContentForm, CarouselForm
from patron.models import *


import dominate
from dominate.tags import *

def index(request):
    return render(request, 'index.html')

def new_carousel(request):
    if request.method == "POST":
        form = CarouselForm(request.POST)
        if form.is_valid():
            carousel = form.save()
            return redirect('carrusel-patron:new_content', carousel.id)
    else:
        form = CarouselForm()
    return render(request, 'new_carousel.html', {'form': form})

def new_content(request, pk):
    carousel = get_object_or_404(Carousel, id=pk)
    count = range(carousel.count)
    if request.method == "POST":
        forms = []
        for i in count:
            forms.append(ContentForm(request.POST, request.FILES, prefix=i))
        for form in forms:
            if form.is_valid():
                content = form.save(commit=False)
                content.carousel = carousel
                content.save()
            else:
                print("invalid")
                redirect('carrusel-patron:new_carousel')
        return redirect('carrusel-patron:generar', carousel.id)
    else:
        forms = []
        for i in count:
            forms.append(ContentForm(prefix=i))
    return render(request, 'new_content.html', {'forms': forms, 'pk':pk})

def generar(request, pk=0):
    carousel = get_object_or_404(Carousel, id=pk)
    elements = carousel.content_set.all().values()
    data = {
        'duration': carousel.timer * 1000,
        'automatic': carousel.auto,
        'circular': carousel.circular,
        'title': carousel.title,
        'elements': elements
    }
    html = armarCarruselHTML(data)
    js = armarCarruselJS(data)
    css = armarCarruselCSS()

    with open('patron/templates/carousel.html', 'w') as f:
        f.write("{% load static %}\n" + html["file"].render())
    with open('static/patron/script.js', 'w') as f:
        f.write(js)
    return render(request, 'carousel.html', {'htmlCode': html["code"].render(), 'cssCode': css})

def armarCarruselHTML(data):
    if data is None:
        return None

    doc = dominate.document(title='Carousel')
    doc2 = dominate.document(title='Carousel')

    with doc.head:
        link(href='https://fonts.googleapis.com/css?family=Alegreya+Sans:300,400|Source+Sans+Pro:400,300', rel='stylesheet', type='text/css')
        link(href="https://fonts.googleapis.com/icon?family=Material+Icons", rel="stylesheet")
        link(rel='stylesheet', href="{% static 'slick/slick.css' %}", type="text/css")
        link(rel='stylesheet', href="{% static 'slick/slick-theme.css' %}", type="text/css")
        link(rel='stylesheet', href="{% static 'prism/prism.css' %}", type="text/css")
        link(rel='stylesheet', href="{% static 'patron/style.css' %}", type="text/css")
    with doc2.head:
        link(href='https://fonts.googleapis.com/css?family=Alegreya+Sans:300,400|Source+Sans+Pro:400,300', rel='stylesheet', type='text/css')
        link(href="https://fonts.googleapis.com/icon?family=Material+Icons", rel="stylesheet")
        link(rel='stylesheet', href="slick/slick.css", type="text/css")
        link(rel='stylesheet', href="slick/slick-theme.css", type="text/css")
        link(rel='stylesheet', href="static/styleCarousel.css", type="text/css")
    
    with doc:
        with div(cls="slider"):
            with div(cls="slides"):
                for e in data['elements']:
                    div(cls="slide").add(img(src="{% static 'images/"+e['image']+"' %}"))
            with div(cls="controls"):
                with div(cls="captions"):
                    for e in data['elements']:
                        div(e['title'], cls="caption")
                div(cls="pagination")
            br()
            h3("Para lograr este carrusel en tu pagina web, solo copia el siguiente codigo:", style="text-align: center;")
            div(pre(code('{{ htmlCode }}', cls="language-html")), cls="code")
        script(type="text/javascript", src="//code.jquery.com/jquery-1.11.0.min.js")
        script(type="text/javascript", src="//code.jquery.com/jquery-migrate-1.2.1.min.js")
        script(type="text/javascript", src="{% static 'slick/slick.min.js' %}")
        script(type="text/javascript", src="{% static 'prism/prism.js' %}")
        script(type="text/javascript", src="{% static 'patron/script.js' %}")
    with doc2:
        with div(cls="slider"):
            with div(cls="slides"):
                for e in data['elements']:
                    div(cls="slide").add(img(src="static/images/"+e['image']))
            with div(cls="controls"):
                with div(cls="captions"):
                    for e in data['elements']:
                        div(e['title'], cls="caption")
                div(cls="pagination")
        script(type="text/javascript", src="//code.jquery.com/jquery-1.11.0.min.js")
        script(type="text/javascript", src="//code.jquery.com/jquery-migrate-1.2.1.min.js")
        script(type="text/javascript", src="slick/slick.min.js")
        script(type="text/javascript", src="static/script.js")
    return { 'file': doc, 'code': doc2 }

def armarCarruselJS(data):
    slides = """
$('.slides').slick({{
    asNavFor: '.captions',
    infinite: {},
    speed: 300,
    autoplay: {},
    autoplaySpeed: {},
    arrows: false,
}}); 
""".format(str(data['circular']).lower(), str(data['automatic']).lower(), data['duration'])

    captions = """
$(".captions").slick({{
    asNavFor: '.slides',
    infinite: {},
    speed: 300,
    fade: true,
    appendArrows: $('.pagination'),
    prevArrow: '<div class="pagination__button"><i class="material-icons">keyboard_arrow_left</i></div>',
    nextArrow: '<div class="pagination__button"><i class="material-icons">keyboard_arrow_right</i></div>'
}});""".format(str(data['circular']).lower())

    return slides + captions

def armarCarruselCSS():
    return """
* {
  box-sizing: border-box;
}
.code{
  height: 300px;
  overflow-y: auto;
}
.slider {
  width: 100%;
  max-width: 700px;
}
.slides {
  background: #ccc;
}
.slide {
  display: flex !important;
  justify-content: center;
  align-items: center;
  background: #fff;
  height: 400px;
  width: 700px;
  outline: 0 !important;
  color: #ccc;
  font-size: 40px;
}
.controls {
  display: flex;
  width: 100%;
}
.captions {
  flex: 1;
  width: 100px;
  padding: 10px;
  margin-top: 2px;
  color: #7b7b7b;
  background: #fff;
}
.caption {
  outline: 0 !important;
}
.pagination {
  display: flex;
  margin-top: 2px;
}
.pagination__button {
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ccc;
  background: #fff;
  width: 40px;
  height: 40px;
  margin-left: 2px;
}
.pagination__button:hover {
  color: #fff;
  background: #2aa1c0;
}
.pagination__button.slick-disabled {
  cursor: not-allowed;
  background: #ccc;
  color: #fff;
}
"""