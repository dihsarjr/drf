from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField()
    @property
    def get_discount(self):
        try:
            return self.price - (self.price/2)
        except:
            return None
    
