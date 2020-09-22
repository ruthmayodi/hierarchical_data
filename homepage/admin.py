from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Name

# Register your models here.
admin.site.register(Name, DraggableMPTTAdmin)
