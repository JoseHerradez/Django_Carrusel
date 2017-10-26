from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # for i in range(0, 30):
    #     new_user = User(username=str(i), first_name=str(i), email=str(i) + '@gmail.com')
    #     new_user.save()
    contact_list = ['John', 'Paul', 'George', 'Ringo']
    paginator = Paginator(contact_list, 2) # Show 2 contacts per page

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'contacts': contacts})
