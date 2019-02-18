from django.db import models

# Create your models here.
class user(models.Model):
	email = models.CharField(max_length=120)
	username = models.CharField(max_length=50)
	last_login = models.CharField(max_length=60)