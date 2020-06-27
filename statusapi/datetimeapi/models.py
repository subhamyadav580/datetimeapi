from django.db import models

"""
creating model fields
"""

class Parameter(models.Model):
    date = models.DateTimeField('Date', blank=True, null=True)
