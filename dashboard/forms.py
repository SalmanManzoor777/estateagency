from django import forms

from home.models import *


# class ListingForm(forms.ModelForm):
#     class Meta:
#         model = Listing
#         fields = ('title', 'description', 'document', )


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','description', 'document', )