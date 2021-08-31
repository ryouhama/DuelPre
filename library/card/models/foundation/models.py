from django.db import models

class CommonModel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
