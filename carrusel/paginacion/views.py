from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from paginacion.models import Elemento

def listing(request):
   
    listaelementos = ['1','2','3',4,5,6,4,78,9,9,9,1,55,9]
    paginator = Paginator(listaelementos, 10) # Show 10 per page

    page = request.GET.get('paginacion')
    try:
        elementos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        elementos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        elementos = paginator.page(paginator.num_pages)

    return render(request, 'paginacion.html', {'elementos': elementos})
