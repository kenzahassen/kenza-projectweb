from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone

number_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="Le numéro doit contenir exactement 8 chiffres.",
)


def validate_birth_date(v):
    if v >= timezone.localdate():
        raise ValidationError(
            "La date de naissance doit être antérieure à la date actuelle."
        )


class Speciality(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    pass


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)],
    )
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField(
        Speciality,
        related_name="doctors",
    )


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[number_validator],
    )
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)