from django.db import models

# Create your models here.
class UserBookmarks(models.Model):
    email = models.CharField(max_length=300)
    news = models.CharField(max_length=300)
    source = models.CharField(max_length=700)
    image = models.CharField(max_length=700)

    def __str__(self):
        return self.email