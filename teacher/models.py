from django.db import models

#
# class Student(models.Model):
#     std_id = models.AutoField(primary_key=True)
#     studentname = models.CharField(max_length=20)
#     studentphone = models.CharField(max_length=20)
#     image = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'student'




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

# class Teacher(models.Model):
#     t_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     address = models.CharField(max_length=30)
#     phone = models.CharField(max_length=12)
#     email = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'teacher'



class Notes(models.Model):
    n_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    note = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'notes'
