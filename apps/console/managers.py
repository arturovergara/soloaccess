# Django Imports
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_active, is_staff, is_superuser, **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email address")

        now = timezone.now()
        normalized_email = self.normalize_email(email)
        user = self.model(
            email=normalized_email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)
