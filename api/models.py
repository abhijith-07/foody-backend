from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    text = models.CharField(max_length=500)
    #image
    MEAL_TYPES = [
        ("dinner","dinner"),
        ("breakfast","breakfast"),
        ("lunch", "lunch")
    ]
    type = models.CharField(max_length=10, choices=MEAL_TYPES)