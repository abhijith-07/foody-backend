from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    MEAL_TYPES = [
        ("dinner","dinner"),
        ("breakfast","breakfast"),
        ("lunch", "lunch")
    ]
    type = models.CharField(max_length=10, choices=MEAL_TYPES)

    def __str__(self):
        return self.name