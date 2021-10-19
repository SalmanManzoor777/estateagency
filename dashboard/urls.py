from django.urls import include, path

from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('upload', file_upload, name='form'),

]
