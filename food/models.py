from django.db import models

# Create your models here.

class item(models.Model):
    item_name = models.TextField(max_length=200)
    item_desc = models.TextField(max_length=200)
    item_price = models.IntegerField()

