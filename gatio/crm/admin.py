from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Screen)
admin.site.register(Contract)
admin.site.register(Advertisement)
admin.site.register(ScreenSpecifications)
admin.site.register(MediaContent)
admin.site.register(Client)
