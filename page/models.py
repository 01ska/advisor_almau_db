from django.db import models

class bachelor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    course = models.IntegerField()
    specialization = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    class Meta:
        db_table = 'bachelor'  # Указываем имя таблицы в базе данных
