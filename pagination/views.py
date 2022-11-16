from multiprocessing import context
from django.shortcuts import render
from .models import *
# Add these imports at the top of your View file
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

# Create your views here.
def home(request):
    # Then, in the view, such as the get_context method:

    # Get page number from request, 
    # default to first page
    default_page = 1
    page = request.GET.get('page', default_page)

    # Get queryset of items to paginate
    services = Service.objects.all()

    # Paginate items
    items_per_page = 2
    paginator = Paginator(services, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    # Provide filtered, paginated library items
    # context["items_page"] = items_page
    

    context = {
        'services':services,
        'items_page':items_page,
    }
    return render(request, 'home.html', context)