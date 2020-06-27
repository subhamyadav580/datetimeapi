from django.db import models

# Create your models here.


class Parameter(models.Model):
    # name = models.CharField('Name', max_length=40, blank=True, null=True)
    date = models.DateTimeField('Date', blank=True, null=True)
