from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

#from ..decorators import teacher_required
from ..forms import OwnerSignUpForm
from ..models import Vistor, User, Realtor

class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'app/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Acoount created Successfully!')
        login(self.request, user)
        return redirect('owner:owner_list')


class RealtorListView(ListView):
    model = Realtor
    ordering = ('name', )
    context_object_name = 'name'
    template_name = 'app/owner/owner.html'
