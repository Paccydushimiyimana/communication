from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    phone = models.IntegerField(null=True,default=True)
    category = models.CharField(max_length=20, null=True)
    student = models.CharField(max_length=20, null=True)
    regNo=models.IntegerField(null=True,default=True)
    lecturer = models.CharField(max_length=20, null=True)
    staffId=models.IntegerField(null=True,default=True)
    college_council = models.CharField(max_length=30, null=True)
    academic_council = models.CharField(max_length=30, null=True)
    school_council=models.CharField(max_length=30, null=True)
    department_council=models.CharField(max_length=30, null=True)
    school=models.CharField(max_length=30, null=True)
    department=models.CharField(max_length=30, null=True)
    level=models.CharField(max_length=30, null=True)

class Category(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Student_category(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Lecturer_category(models.Model): 
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name       

class College_council(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class School_council(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Department_council(models.Model):
    name=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name       

class Academic_council(models.Model):
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name 

class College(models.Model):
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class School(models.Model):
    name=models.CharField(max_length=20, unique=True)
    college=models.ForeignKey(College, related_name='schools', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=30, unique=True)
    school=models.ForeignKey(School, related_name='departments',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    name=models.CharField(max_length=1)  
    department=models.ForeignKey(Department, related_name='levels', on_delete=models.SET_NULL, null=True)      

    def __str__(self):
        return self.name    

