from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from paginacion.paginator import *
from django.urls import reverse_lazy

def index(request):
    # for i in range(0, 30):
    #     new_user = User(username=str(i), first_name=str(i), email=str(i) + '@gmail.com')
    #     new_user.save()
    contact_list = ['John', 'Paul', 'George', 'Ringo']
    numberOfElements = 2
    page = request.GET.get('page', 1)
    if request.method == "POST":
        numberOfElements = request.POST.get('numberOfElements', 2)
    else:
        numberOfElements = request.GET.get('show', 2)
    paginator = TUIsDPaginator(contact_list, int(numberOfElements))
    contacts = paginator.get_elems_from_page(page)
    return render(request, 'list.html', {'contacts': contacts, 'number': abs(contacts.end_index() - contacts.start_index())+1})
