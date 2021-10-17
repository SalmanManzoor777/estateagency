from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages


class SignUpView(TemplateView):
    template_name = 'app/signup.html'


# class LoginView(TemplateView):
#     template_name = 'app/login.html'


def home(request):
    

    if request.user.is_authenticated:

        if request.user:
            return render(request, 'app/home.html')
        

        if request.user.is_buyer:
            return redirect('buyer:realtor_list')
        elif request.user.is_owner:
            return redirect('owner:owner_list')
        else:
            return HttpResponse('You have to log in')

    return render(request, 'app/home.html')
