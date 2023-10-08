from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=80, null=True)
    category = models.CharField(max_length=80)
    price = models.IntegerField()
    availability = models.BooleanField()
    created_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.price} - {self.created_date}'

    def get_absolute_url(self):
        return reverse('factory1:product_detail1', args=[str(self.pk)])
