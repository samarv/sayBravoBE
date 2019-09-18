from django.contrib import admin
from .models import organizations, users, shoutouts

admin.site.register(organizations)
admin.site.register(users)
admin.site.register(shoutouts)
