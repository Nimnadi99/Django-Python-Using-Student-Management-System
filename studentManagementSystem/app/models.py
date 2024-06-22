from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Course = models.CharField(max_length=255)
    Age = models.IntegerField()
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=10)
    NIC = models.CharField(max_length=12) 

    def __str__(self):
        return str(self.id)