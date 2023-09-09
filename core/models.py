from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class EVChargingLocation(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name




att_option = (
    ("xxx", "xxx"),
    ("xxx", "xxx"),
) 


class Review(models.Model):
    address = models.CharField(max_length=255)
    attributes = models.CharField(max_length=255, choices=att_option)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    pos_text = models.CharField(max_length=500)
    neg_text = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)


# class User(models.Model):
#     username = models.CharField(max_length=24)
#     password = models.CharField()
#     attributes = models.CharField(choices=att_option)





