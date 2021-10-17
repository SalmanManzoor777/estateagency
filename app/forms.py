from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from app.models import (Vistor, User)

class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        return user


class BuyerSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_buyer = True
        user.save()
#        vistor = Vistor.objects.create(user=user)

        return user
