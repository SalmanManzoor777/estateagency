from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db import models
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

#from ..decorators import student_required
from ..forms import  BuyerSignUpForm
from ..models import Vistor, User, Realtor


class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'app/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Acoount created Successfully!')
        login(self.request, user)
        return redirect('home')



class RealtorListView(ListView):
    model = Realtor
    ordering = ('name', )
    context_object_name = 'name'
    template_name = 'app/buyer/buyer.html'
