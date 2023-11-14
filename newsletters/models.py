from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
   

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    subscribers = models.ManyToManyField(Subscriber, related_name='subscribed_newsletters')
    created_at = models.DateTimeField(auto_now_add=True)


