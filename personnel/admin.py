from django.contrib import admin
from personnel.models import User
from flotte.models import Vehicule

# Register your models here.

admin.site.register(User)
admin.site.register(Vehicule)