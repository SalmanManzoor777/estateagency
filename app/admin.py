from django.contrib import admin

from app.models import Realtor, User, Vistor

# Register your models here.
admin.site.register(User)
admin.site.register(Vistor)
admin.site.register(Realtor)