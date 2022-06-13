from cgitb import html
import re
from urllib import request
from django.shortcuts import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'listings/band_list.html',
    {"bands": bands})

def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id) # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
    'listings/band_detail.html',
    {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def about(request):
    return HttpResponse('<h1>À propos</h1> <p> Nous adorons merch ! </p>')

def contact(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p> Merci de remplir le formulaire </p>')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
    'listings/listing_list.html',
    {"listings": listings})

def listing_detail(request, id):  # notez le paramètre id supplémentaire
    listing = Listing.objects.get(id=id) # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
    'listings/listing_detail.html',
    {"listing": listing}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def contact(request):
    # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject = f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message = form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-envoye')
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
    'listings/contact.html',
    {'form': form})
