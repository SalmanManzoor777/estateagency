from django.http import response
from home.models import *
from dashboard.forms import  DocumentForm
from django.shortcuts import render, redirect
from django.http import (HttpResponse, HttpResponseBadRequest, 
                         HttpResponseForbidden)
# Create your views here.


def dashboard(request):
    return render(request, 'home.html')


# def form_upload(request):
#     if request.method == 'POST':


#         form = ListingForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ListingForm()
#     return render(request, 'forms.html', {
#         'form': form
#     })


def file_upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('form is saved:')
            return redirect('home')
        else:
            return HttpResponseBadRequest('This view can not handle method {0}'.\
                                      format(request.method), status=405)
    else:
        form = DocumentForm()
    return render(request, 'forms.html', {
        'form': form
    })
