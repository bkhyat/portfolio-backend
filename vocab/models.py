from django.db import models

# Create your models here.


class VocabSource(models.Model):
    source = models.CharField(max_length=100)
    sheet = models.CharField(max_length=50, null=True, blank=True)


class Page(models.Model):
    page = models.IntegerField()
    vocab_source = models.ForeignKey(VocabSource, on_delete=models.CASCADE)


class Word(models.Model):
    word = models.CharField(max_length=100)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.word