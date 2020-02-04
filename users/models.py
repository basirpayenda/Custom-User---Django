from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    DEGREE_CHOICE = (
        ('Graduated', 'Graduated'),
        ('Freshman', 'Freshman'),
        ('Master Degree', 'Master Degree'),
        ('PHD', 'PHD')
    )

    phoneNumber = models.CharField(
        verbose_name='Phone Number', max_length=20, null=True, blank=True)
    jobTitle = models.CharField(
        verbose_name='Job Title', max_length=200, null=True, blank=True)
    zipCode = models.CharField(
        verbose_name='Zip Code', max_length=10, null=True, blank=True)
    degree = models.CharField(
        max_length=15, choices=DEGREE_CHOICE, null=True, blank=True)
