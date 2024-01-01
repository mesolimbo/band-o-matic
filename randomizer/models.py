from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=100)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
