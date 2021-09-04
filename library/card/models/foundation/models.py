from django.utils import timezone
from django.db import models


class CommonModel(models.Model):
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
