from django.urls import include, path

from .views import views, buyer, owner


urlpatterns = [
    path('', views.home, name='home'),

    path('buyer/', include(([
        path('', buyer.RealtorListView.as_view(), name='realtor_list'),

    ], 'app'), namespace='buyer')),


    # Path for Property Owner
    path('owner/', include(([
        path('', owner.RealtorListView.as_view(), name='owner_list'),
    ], 'app'), namespace='owner')),

]
