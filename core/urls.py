
from django.contrib import admin
from django.urls import path, include
from app.views import buyer, owner, views
from home.views import *
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
#    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/buyer/', buyer.BuyerSignUpView.as_view(), name='buyer_signup'),
    path('accounts/signup/owner/', owner.OwnerSignUpView.as_view(), name='owner_signup'),
]
