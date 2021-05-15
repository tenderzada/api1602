from django.contrib import admin

# Register your models here.

from .models import Receiver, Alert


admin.site.register(Receiver)
admin.site.register(Alert)