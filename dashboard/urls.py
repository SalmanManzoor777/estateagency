from django.urls import include, path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('form', form, name='form'),

]
