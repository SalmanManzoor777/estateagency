from home.models import *
from dashboard.forms import ListingForm
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    return render(request, 'index.html')


def form_upload(request):
    if request.method == 'POST':


        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListingForm()
    return render(request, 'forms.html', {
        'form': form
    })


def form(request):
    return render(request, 'forms.html')
