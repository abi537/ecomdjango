from django.db import models

# Create your models here.
from customers.models import Customer
from products.models import Product
# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=(LIVE,'LIVE'),(DELETE,'DELETE')
    CART_STAGE=0
    ORDER_CONFTRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED"))

    order_status=(models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE))
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders',null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return super().__str__()

class Ordereditem(models.Model):
    product=models.ForeignKey(Product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,related_name='added_items',on_delete=models.CASCADE)
