from django.db import models
class MyJournal(models.Model):
    date_created = models.DateField('journal date')
    content = models.TextField()
# Create your models here.
