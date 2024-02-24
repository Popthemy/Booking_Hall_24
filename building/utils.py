from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Hall



def search_halls(request):
    ''' param: request
    get search query from the request
    return:
    search_query: to help fill the user input box when a search exists and to help us filter our hall
    halls: query set of matched items after filtering'''
    # getting search query
    search_query = request.GET.get('search_query', '')

    # filtering based on search
    halls = Hall.objects.distinct().filter(Q(name__icontains=search_query)
                                           | Q(location__icontains=search_query))
    return search_query, halls



def paginate_halls(request,halls,result):
    ''' function for pagination and error handling'''

    page = request.GET.get('page', 1)

    paginated_halls_query = Paginator(halls, result)


    try:
        paginated_page = paginated_halls_query.page(page)
    except PageNotAnInteger:
        page = 1 
        paginated_page = paginated_halls_query.page(page)
    except EmptyPage:
        page = paginated_halls_query.num_pages # gets the last page
        paginated_page = paginated_halls_query.page(page)

    return paginated_page

    

