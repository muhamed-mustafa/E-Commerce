from django.db import models
from django.utils.translation import ugettext_lazy as _
from product.models import Product
# Create your models here.

class Order(models.Model):
    first_name  = models.CharField(max_length=100,verbose_name=_('First Name'))
    last_name   = models.CharField(max_length=100,verbose_name=_('Last Name'))
    email       = models.EmailField(verbose_name=_('Email'))
    address     = models.CharField(max_length=100,verbose_name=_('Address'))
    postal_code = models.CharField(max_length=100,verbose_name=_('Postal Code'))
    city        = models.CharField(max_length=100,verbose_name=_('City'))
    created     = models.DateTimeField(auto_now_add=True,verbose_name=_('Created'))
    updated     = models.DateTimeField(auto_now=True,verbose_name=_('Updated'))
    paid        = models.BooleanField(default=False,verbose_name=_('Paid'))

    
    class Meta :
        ordering            = ('-created',)
        verbose_name        = _('Order')
        verbose_name_plural = _('Orders')

    
    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    
class OrderItem(models.Model):
    order    = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE,verbose_name=_('Order'))
    product  = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE,verbose_name=_('Product'))
    price    = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_('Price'))
    quantity = models.PositiveIntegerField(default=1,verbose_name=_('Quantity'))


    class Meta :
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    
    def __str__(self) :
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
