from django.db import models
from datetime import datetime
# Create your models here.
class ProductDetails(models.Model):
    SPORTS="SPORTS"
    WINTER = "WINTER"
    SUMMER = "SUMMER"
    CATEGORY=[
        (SPORTS,"sports"),
        (WINTER,"winter"),
        (SUMMER,"summer")
    ]
    M="M"
    S="S"
    L="L"
    XL="XL"
    SIZE=[
        (M,"medium"),
        (S,"small"),
        (L,"large"),
        (XL,"extra large")
    ]
    name=models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    size = models.CharField(choices=SIZE,default=M,null=True,max_length=10)
    category = models.CharField(choices=CATEGORY,default=SPORTS,null=True,max_length=10)
    quantity=models.IntegerField(default=1)
    created_on = models.DateTimeField(default=datetime.now(),blank=True)

class Customer(models.Model):
    name=models.CharField(max_length=20)
    product=models.ForeignKey('ProductDetails',on_delete=models.CASCADE,null=True,blank=True)






