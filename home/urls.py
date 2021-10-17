from django.urls import include, path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('agent', agentone, name='agent'),
    path('agentall', agentall, name='agentall'),
    path('contact', contact, name='contact'),
    path('property', propertyone, name='property'),
    path('propertyall', propertyall, name='propertyall'),
]
