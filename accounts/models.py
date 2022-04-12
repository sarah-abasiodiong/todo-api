from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    


def __str__(self):
        return self.title

