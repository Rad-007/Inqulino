from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class about:
    id:int
    name:str
    details:str


# Create your models here.

'''

class User(AbstractUser):
    paid_until=models.DateField(
        null=True,
        blank=True)

    def has_paid (self,
        current_date =datetime.date.today ()):

             
        return current_date<self.paid_until
        '''



from django.db import models
from django.core import validators

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=70,
        verbose_name='Product Name'
    )

    description = models.TextField(
        max_length=800,
        verbose_name='Description'
    )

    price = models.IntegerField(1000)



    def __str__(self) :
        return self.name


class OrderDetail(models.Model):

    id = models.BigAutoField(
        primary_key=True
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    product = models.ForeignKey(
        to=Product,
        verbose_name='Product',
        on_delete=models.PROTECT
    )

    amount = models.IntegerField(
        verbose_name='Amount'
    )

    stripe_payment_intent = models.CharField(
        max_length=200
    )

    # This field can be changed as status
    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )

'''
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
	
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)'''