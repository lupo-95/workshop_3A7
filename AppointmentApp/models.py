from django.db import models
from AccountApp.models import Doctor, Patient
# Create your models here.

class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(upload_to='prescriptions/',
                                     null=True,
                                       blank=True)
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'Appointment_date'],
                name="unique_appointment_per_doctor_per_time",
                violation_error_message="Un rendez-vous existe déjà pour ce médecin à cette date et heure."
            )
        ]