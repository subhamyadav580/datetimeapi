from django.db import models

# Create your models here.


class Parameter(models.Model):
    date = models.DateTimeField('Date', blank=True, null=True)
