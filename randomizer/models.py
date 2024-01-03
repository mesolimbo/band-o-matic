from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def delete(self, *args, **kwargs):
        # Get all the words associated with this category
        words_to_check = self.wordcategory_set.all()

        super(Category, self).delete(*args, **kwargs)

        # After category deletion, check words that don't have any categories left and delete them
        for word in words_to_check:
            if word.categories.count() == 0:
                word.delete()

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=100, unique=True)
    categories = models.ManyToManyField(Category, through='WordCategory')

    def __str__(self):
        return self.name


class WordCategory(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('word', 'category')
