from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from paginacion.paginator import *
from django.urls import reverse_lazy
from paginacion.models import List, ListElem


def index(request):
    list = List(ident=1)
    list.save()
    listElem = ListElem(ident=list, elem='elemento1')
    listElem.save()

    list_id = List.objects.filter(ident=1)[0]
    contact_list = ListElem.objects.filter(ident=list_id)
    numberOfElement = 2
    page = request.GET.get('page', 1)

    if request.method == "POST":
        numberOfElements = request.POST.get('numberOfElements', 2)
        if int(numberOfElements) < 1:
            numberOfElements = "1"

        newElem = request.POST.get('newElem')
        if newElem != None:
            ListElem.objects.create(ident=list_id, elem=newElem)
    else:
        numberOfElements = request.GET.get('show', 2)

    paginator = TUIsDPaginator(contact_list, int(numberOfElements))
    contacts = paginator.get_elems_from_page(page)
    return render(request, 'list.html', {'contacts': contacts, 'number': numberOfElements})
