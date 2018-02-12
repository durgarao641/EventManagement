from django.db import models
import datetime

# Create your models here.

class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=25)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=10)
    mail_id = models.CharField(max_length=30)

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=40)
    branch = models.CharField(max_length=10)

class Events(models.Model):
    event_id = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=25)
    date = models.DateField(default=datetime.date.today)
    organizors = models.CharField(max_length=150)

class Participants(models.Model):
    event_id = models.CharField(max_length=25)
    student_id = models.CharField(max_length=25)
    
class EventWinners(models.Model):
    event_id = models.CharField(primary_key=True, max_length=25)
    first_winner = models.CharField(max_length=25)
    second_winner = models.CharField(max_length=25)
    third_winner = models.CharField(max_length=25)
    
