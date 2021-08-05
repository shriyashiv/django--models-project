# Generated by Django 3.2.5 on 2021-08-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=200)),
                ('MOTHERNAME', models.CharField(max_length=200)),
                ('FATHERNAME', models.CharField(max_length=200)),
                ('NATIONALITY', models.CharField(max_length=200)),
                ('EMAIL', models.EmailField(max_length=200)),
                ('AGE', models.PositiveSmallIntegerField(null=True)),
                ('CONTACTNUMBER', models.CharField(max_length=200)),
                ('ADDRESS', models.CharField(max_length=200)),
                ('GENDER', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('PASSPORTNUMBER', models.CharField(max_length=200)),
                ('SELECT', models.CharField(choices=[('o', 'One way'), ('r', 'Round trip')], max_length=1)),
                ('FROM', models.CharField(max_length=200)),
                ('TO', models.CharField(max_length=200)),
                ('NOOFPASSENGER', models.PositiveSmallIntegerField(null=True)),
                ('DEPARTUREDATE', models.DateField(blank=True, null=True)),
                ('ARRIVALDATE', models.DateField(blank=True, null=True)),
                ('TRAVELCLASS', models.CharField(choices=[('E', 'Economy'), ('PE', 'Premium Economy'), ('B', 'Business'), ('FC', 'First Class'), ('SC', 'Second Class')], max_length=20)),
                ('FLIGHTTYPE', models.CharField(choices=[('G', 'general'), ('P', 'private')], max_length=1)),
                ('SLOT', models.CharField(choices=[('4', '4:00am'), ('6', '6:00am'), ('8', '8:00am'), ('10', '10:00am'), ('12', '12:00pm')], max_length=6)),
            ],
        ),
    ]