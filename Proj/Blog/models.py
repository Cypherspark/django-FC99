from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 100 , null = True, blank = True)
    password = models.CharField(max_length = 100 , null = True, blank = True)

