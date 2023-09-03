from django.db import models


class Alarm(models.Model):
    date = models.DateTimeField()
    oblast = models.CharField(max_length=63)

    def __str__(self):
        return f"Alarm! Date: {self.date}. Oblast: {self.oblast}."


class AlarmEnd(models.Model):
    date = models.DateTimeField()
    oblast = models.CharField(max_length=63)
    alarm = models.OneToOneField(Alarm, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"AlarmEnd! Date: {self.date}. Oblast: {self.oblast}"
