from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']


class Word(models.Model):
    name = models.CharField(max_length=100, unique=True)
    categories = models.ManyToManyField(Category, through='WordCategory')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class WordCategory(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.word} ({self.category})'
        # return f'{str(self.word)} {str(self.category)}'

    class Meta:
        unique_together = ('word', 'category')
        verbose_name_plural = "word categories"
