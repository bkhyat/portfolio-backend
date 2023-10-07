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


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)
    parent_category = models.ForeignKey("Category", models.SET_NULL, null=True, blank=True, related_name="children")

    def __str__(self):
        return f"{self.id} - {self.__repr_category__()}"

    def __repr_category__(self):
        str_ = ""
        category = self.parent_category
        while category:
            str_ += f"{category.category_name} -> "
            category = category.parent_category
        return f"{str_}{self.category_name}"

    def get_associated_words(self):
        qs = Word.objects.none()
        qs = Category.__get_words_recursively(self, self.children.all(), qs)
        return qs

    @staticmethod
    def __get_words_recursively(category, children, qs):
        qs = qs | category.vocabword_set.all()
        for child in children:
            qs = qs | child.vocabword_set.all()
            if nested_children := child.children.all():
                qs = qs | Category.__get_words_recursively(child, nested_children, qs)
        return qs


class VocabWord(models.Model):
    word = models.CharField(max_length=100)
    category = models.ForeignKey("Category", models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.category.__repr_category__()}: {self.word}"
