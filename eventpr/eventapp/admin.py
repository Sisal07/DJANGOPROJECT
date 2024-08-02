from django.contrib import admin
from .models import Venue, Online, Contact

# Register your models here.
admin.site.register(Venue)
admin.site.register(Online)
admin.site.register(Contact)