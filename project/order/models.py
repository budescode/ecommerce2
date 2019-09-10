from django.db import models
from cart.models import Cart
from account.models import Vendor
from django.contrib.auth.models import User


class Order(models.Model):
	choices = (('payment on delivery', 'payment on delivery'),
		('online payment', 'online payment'))
	cart = models.ForeignKey(Cart,on_delete=models.CASCADE , related_name='order_cart')
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='order_vendor')
	email = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='order_user')
	address1 = models.TextField()
	address2 = models.TextField(blank=True, null=True)
	phone_number = models.TextField()
	first_name = models.TextField()
	last_name = models.TextField()
	postcode = models.TextField()
	payment_method = models.CharField(max_length=30, choices=choices)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username