from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=300, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    shipping_price = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    @property
    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return ""
