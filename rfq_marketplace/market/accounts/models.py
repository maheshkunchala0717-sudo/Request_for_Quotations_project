from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role=models.CharField(max_length=20,
                          choices=[('buyer','Buyer'),('supplier','Supplier')])


class RFQ(models.Model):
    product_service=models.CharField(max_length=200)
    description=models.TextField()
    quantity=models.PositiveIntegerField()
    deliver_location=models.CharField(max_length=200)
    dead_line=models.DateField(default='2026-09-30')

    buyer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="rfqs")


    def __str__(self):
        return self.product_service



class Quatation(models.Model):
    rfq=models.ForeignKey(RFQ,on_delete=models.CASCADE,related_name='quatations')
    supplier=models.ForeignKey(User,on_delete=models.CASCADE,related_name='quatations')
    price=models.DecimalField(max_digits=12,decimal_places=2)
    delivery_time=models.PositiveIntegerField()
    notes=models.TextField(blank=True)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
      return self.rfq.product_service



