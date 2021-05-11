from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.TextField(max_length=25, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'book'