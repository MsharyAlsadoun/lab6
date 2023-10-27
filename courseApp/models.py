from django.db import models

# Create your models here.


class course(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.id} : {self.name}"
    
    
    
class Student(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    gpa = models.CharField(max_length=10)
    courses = models.ManyToManyField(course , related_name="students")
    
    def __str__(self):
        return f"{self.id} name: {self.first} {self.last} gpa: {self.gpa}"
    
