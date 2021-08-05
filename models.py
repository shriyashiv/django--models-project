from django.db import models

class Passenger_details(models.Model):
    NAME=models.CharField(max_length=200)
    MOTHERNAME = models.CharField(max_length=200)
    FATHERNAME = models.CharField(max_length=200)
    NATIONALITY = models.CharField(max_length=200)
    EMAIL = models.EmailField(max_length=200)
    AGE = models.PositiveSmallIntegerField(null=True)
    CONTACTNUMBER = models.CharField(max_length=200)
    ADDRESS= models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    GENDER = models.CharField(max_length=1, choices=GENDER_CHOICES)

    PASSPORTNUMBER = models.CharField(max_length=200)
    SELECT_CHOICES = (
        ('o', 'One way'),
        ('r', 'Round trip'),
    )
    SELECT = models.CharField(max_length=1, choices=SELECT_CHOICES)
    FROM = models.CharField(max_length=200)
    TO=models.CharField(max_length=200)
    NOOFPASSENGER = models.PositiveSmallIntegerField(null=True)
    DEPARTUREDATE=models.DateField(null=True,blank=True)
    ARRIVALDATE = models.DateField(null=True,blank=True)
    TRAVEL_CHOICES=(
        ('E', 'Economy'),
        ('PE', 'Premium Economy'),
        ('B', 'Business'),
        ('FC', 'First Class'),
        ('SC', 'Second Class'),

    )
    TRAVELCLASS = models.CharField(max_length=20, choices=TRAVEL_CHOICES)
    FLIGHT_CHOICES = (
        ('G', 'general'),
        ('P', 'private'),
    )
    FLIGHTTYPE = models.CharField(max_length=1, choices=FLIGHT_CHOICES)
    SLOT_CHOICES = (
        ('4', '4:00am'),
        ('6', '6:00am'),
        ('8', '8:00am'),
        ('10', '10:00am'),
        ('12', '12:00pm'),
    )
    SLOT = models.CharField(max_length=6, choices=SLOT_CHOICES)

    def __str__(self):
        return self.NAME
# Create your models here.

