from cgitb import html
from urllib import request
from django.shortcuts import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'listings/band_list.html',
    {"bands": bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
    'listings/band_detail.html',
    {'band': band})


def about(request):
    return HttpResponse('<h1>À propos</h1> <p> Nous adorons merch ! </p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p> Merci de remplir le formulaire </p>')

def listing(request):
    listings = Listing.objects.all()
    return render(request,
    'listings/listing.html',
    {"listings": listings})
