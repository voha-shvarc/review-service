from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    slug = models.Model
    link = models.URLField()

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField()
    author_email = models.EmailField()

    def __str__(self):
        return self.title
