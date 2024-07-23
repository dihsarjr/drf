from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=99.00, max_digits=15, decimal_places=2,)
    @property
    def get_discount(self):
        return self.price - (self.price/2)
