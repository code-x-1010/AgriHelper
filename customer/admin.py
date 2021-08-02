from django.contrib import admin

from .models import details, credentials, log_user

# Register your models here.
admin.site.register(details)
admin.site.register(credentials)
admin.site.register(log_user)
