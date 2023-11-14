from django.db import models

# Create your models here.


class Trade(models.Model):
    transaction= models.CharField(max_length=50)
    rate=models.BigIntegerField()
    min=models.BigIntegerField()
    Max=models.BigIntegerField()
    status=models.CharField(max_length=50)

class GiftCard(models.Model):
    transaction= models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    rate=models.BigIntegerField()
    min=models.BigIntegerField()
    Max=models.BigIntegerField()
    status=models.CharField(max_length=50)
    variant=models.CharField(max_length=50)





