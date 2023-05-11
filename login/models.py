from django.db import models

# Create your models here.

class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'student'

class Teacher(models.Model):
    t_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'teacher'


class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'
