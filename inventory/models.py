from django.db import models


class Category(models.Model):
    """Implementation of Category model."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
