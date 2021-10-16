from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    avatar = models.CharField(max_length=700)

    def __str__(self):
        return self.name