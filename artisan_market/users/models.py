from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, name, lastname, password, picture, biography, **other_fields): # TODO: Poner el role_id cuando añada las relaciones
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)

        user = self.model(email=email, name=name, lastname=lastname, picture=picture, biography=biography, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, lastname, password, picture, biography, **other_fields): # TODO: Poner el role_id cuando añada las relaciones
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, lastname, password, picture, biography, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    picture = models.ImageField(upload_to='users/', blank=True)
    biography = models.TextField(blank=True)
    # TODO: Poner el role_id cuando añada las relaciones
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'lastname', 'picture', 'biography']
