from django.shortcuts import render

from listings.models import Listing

def index(request):
    listings = Listing.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': listings
    }


    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
