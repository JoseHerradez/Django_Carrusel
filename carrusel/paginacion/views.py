from django.shortcuts import render
from paginacion.paginator import *

def index(request):
    # for i in range(0, 30):
    #     new_user = User(username=str(i), first_name=str(i), email=str(i) + '@gmail.com')
    #     new_user.save()
    contact_list = ['John', 'Paul', 'George', 'Ringo']
    #paginator = Paginator(contact_list, 2) # Show 2 contacts per page
    paginator2 = TUIsDPaginator(contact_list, 2)
    
    page = request.GET.get('page', 1)
    contacts = paginator2.get_elems_from_page(page)
	
    return render(request, 'list.html', {'contacts': contacts})
   

	
