from django.db import models

# Create your models here.
class Comment(models.Model):
	comment = models.TextField()
	user = models.CharField(max_length=25)
    