from django import forms

from home.models import *


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'document', )
