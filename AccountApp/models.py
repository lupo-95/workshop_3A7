from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class User(AbstractUser):
    pass
class Specialty(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    specialities=models.ManyToManyField(
        Specialty,
        related_name="doctors"
        )
number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="le numero est incorrect !ne pas respecter le pattern 8 chiffres exacte "
        )
def validate_birth_date(v):
    if v >= timezone.localdate():
        raise ValidationError("La date de naissance ne peut pas être dans le futur.")
class Patient(User):
    national_id = models.CharField(max_length=8,unique=True,validators=[number_validator])
    phone=models.CharField(max_length=8,validators=[number_validator])
    birth_date=models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)