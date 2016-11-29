from django.db import models


class Category(models.Model):
    """Implementation of Category model."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Implementation of Book model."""

    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'authors')
