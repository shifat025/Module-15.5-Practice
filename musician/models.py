from django.db import models

# Create your models here.

class musicians(models.Model):
    First_name = models.CharField( max_length=50)
    Last_name = models.CharField( max_length=50)

    email = models.EmailField()
    phone_number = models.IntegerField()
    Instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return self.First_name