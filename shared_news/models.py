from django.db import models

# Create your models here.


class SharedNews(models.Model):
    news = models.CharField(max_length=300)
    source = models.CharField(max_length=700)
    image = models.CharField(max_length=700)

    def __str__(self):
        return self.news
