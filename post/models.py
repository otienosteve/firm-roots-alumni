from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True)
    title= models.CharField("Title",max_length=50)
    body = models.TextField("Post")
    date_posted = models.DateField("DATE CREATED",auto_now=False, auto_now_add=False)
    


