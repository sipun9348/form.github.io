from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    def __str__(self):
        return self.name

    
