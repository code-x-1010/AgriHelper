from django.contrib import admin

from .models import sale, inspect, procurement

# Register your models here.

admin.site.register(inspect)
admin.site.register(sale)
admin.site.register(procurement)
