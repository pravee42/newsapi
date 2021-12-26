from django.db import models

# Create your models here.


class Atricles(models.Model):
    author = models.CharField(max_length=300)
    published_date = models.DateField(auto_now_add=True)
    votes = models.IntegerField()
    title = models.CharField(max_length=500)
    article = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
