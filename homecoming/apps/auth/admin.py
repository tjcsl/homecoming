from django.contrib import admin

from .models import ClassGroup, User

admin.site.register(User)
admin.site.register(ClassGroup)
