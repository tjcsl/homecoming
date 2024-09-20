from django.contrib import admin

from .models import ClassGroup, User


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "is_staff", "is_hoco_admin", "is_class_group_admin"]
    list_filter = ["is_hoco_admin", "is_class_group_admin", "is_staff", "is_superuser", "is_student", "is_teacher"]
    search_fields = ["username", "first_name", "last_name"]

admin.site.register(User, UserAdmin)
admin.site.register(ClassGroup)
