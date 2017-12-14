from django.db import models
from django.contrib.auth.models import User

class submissions(models.Model):
    topic=models.CharField(max_length=50)
    date=models.DateTimeField()
    def __str__(self):
        return str(self.date) + " : " + str(self.topic)
    class Meta:
        ordering = ["date"]

class Group(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
