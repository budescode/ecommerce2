from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='subcategory')
	subcategory = models.CharField(max_length=100)
	def __str__(self):
		return self.subcategory

class Brand(models.Model):
	name=models.CharField(max_length=100)
	image = models.ImageField()

class Vendor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	company_name = models.CharField(max_length=100)
	business_name = models.CharField(max_length=100, help_text='Registered business name')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.IntegerField()
	address_line_1 = models.CharField(max_length=200)
	address_line_2 = models.CharField(max_length=200, blank=True, null=True)
	state = models.CharField(max_length=40)
	country = models.CharField(max_length=40)
	active = models.BooleanField(default=False)

class VendorPost(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)	
	name = models.CharField(max_length=60)
	description = models.TextField()
	price = models.IntegerField()
	available_products = models.IntegerField()
	image1 = models.ImageField(null=True, blank=True)
	image2 = models.ImageField(null=True, blank=True)
	image3 = models.ImageField(null=True, blank=True)
	image4 = models.ImageField(null=True, blank=True)
	image5 = models.ImageField(null=True, blank=True)
	color = models.TextField(null=True, blank=True)


