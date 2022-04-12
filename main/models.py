from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    updated_at = models.DateTimeField( auto_now_add= True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()



def __str__(self):
        return self.title

