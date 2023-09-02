from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

    is_teacher = models.BooleanField(default=False, null=False)
    is_student = models.BooleanField(default=True, null=False)
    is_class_group_admin = models.BooleanField(default=False, null=False)
    is_hoco_admin = models.BooleanField(default=False, null=False)

    @property
    def class_group(self):
        for class_group in ClassGroup.objects.all():
            if class_group.has_user(self):
                return class_group

        return None

    @property
    def has_management_permission(self) -> bool:
        return (
            self.is_hoco_admin or self.is_teacher or self.is_staff or self.is_superuser
        )

    @property
    def short_name(self):
        return self.username

    def get_social_auth(self):
        return self.social_auth.get(provider="ion")

    def __str__(self):
        return self.short_name


class ClassGroup(models.Model):
    name = models.CharField(max_length=128)
    username_prefix = models.CharField(max_length=4)  # e.g. "2024"

    message = models.TextField(max_length=48000, blank=True, null=True)

    def has_user(self, user: User) -> bool:
        return user.username.startswith(self.username_prefix)

    def __str__(self):
        return self.name
