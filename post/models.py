from django.db import models


# Create your models here.



class Post(models.Model):
    name = models.CharField(max_length=20)
    price = models.SmallIntegerField()

    def __str__(self):
        return self.name