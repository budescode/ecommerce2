from django.db import models
from django.contrib.auth.models import User
from account.models import Vendor
from administrator.models import Category, SubCategory, Brand

class Cart(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='cartuser')
	Product_title = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	subcategory = models.CharField(max_length=100)	
	brand = models.CharField(max_length=100)
	# unit = models.CharField(max_length=30, help_text='Unit(e.g Kg, Pc, Etc')
	# tags = models.CharField(max_length=30)
	description = models.TextField()
	single_price = models.DecimalField(decimal_places=2, max_digits=15)
	price = models.DecimalField(decimal_places=2, max_digits=15)
	image1 = models.TextField()
	color=models.CharField(max_length=20, default='')
	quantity = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)
	paid = models.BooleanField(default=False)
	order = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username