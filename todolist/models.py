from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    class Meta:

        db_table = 'task'

    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    done = models.BooleanField()
    
    def __str__(self):
        return self.name