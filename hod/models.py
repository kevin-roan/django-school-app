from django.db import models

# Create your models here.

class Hod(models.Model):
    h_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hod'
