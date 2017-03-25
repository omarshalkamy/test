from django.db import models

class location(models.Model):
    name=models.CharField(max_length=30)
    long=models.FloatField(max_length=20)
    lag=models.FloatField(max_length=25)
    bt=models.BooleanField(max_length=5)
    accel=models.BooleanField(max_length=5)
    gyro=models.BooleanField(max_length=5)
    def __str__(self):
        return self.name