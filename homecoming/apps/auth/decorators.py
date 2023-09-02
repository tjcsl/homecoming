from django.contrib.auth.decorators import user_passes_test

management_only = user_passes_test(
    lambda u: u.is_authenticated and u.has_management_permission  # type: ignore
)

management_or_class_group_admin_only = user_passes_test(
    lambda u: u.is_authenticated
    and (u.has_management_permission or u.is_class_group_admin)
)
