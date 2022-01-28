from django.db import models

# Create your models here.


class Articles(models.Model):
    author = models.CharField(max_length=300)
    published_date = models.DateField(auto_now_add=True)
    votes = models.IntegerField()
    title = models.CharField(max_length=500)
    article = models.CharField(max_length=10000)
    creater_email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.CharField(max_length=300)
    article_id = models.IntegerField(default=0)
    commented_date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=10000)
    likes = models.IntegerField()

    def __str__(self):
        return self.user
