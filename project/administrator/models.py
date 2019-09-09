from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 
from account.models import Vendor

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
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brand_category')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='brand_subcategory')
	name=models.CharField(max_length=100)
	image = models.ImageField()
	def __str__(self):
		return self.name



class VendorPost(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1, related_name='vendor_related_name')
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='vendoruser')
	Product_title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='vendorcategory')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1, related_name='vendorsubcategory')	
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	unit = models.CharField(max_length=30, help_text='Unit(e.g Kg, Pc, Etc')
	tags = models.CharField(max_length=30)
	description = RichTextUploadingField()
	price = models.DecimalField(decimal_places=2, max_digits=15)
	available_products = models.CharField(max_length=200)
	image1 = models.ImageField(default='')
	image2 = models.ImageField(null=True, blank=True, default='')
	sale_price = models.DecimalField(decimal_places=2, max_digits=15)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=15)
	shipping_cost = models.DecimalField(decimal_places=2, max_digits=15)
	product_tax = models.DecimalField(decimal_places=2, max_digits=15)
	product_discount = models.DecimalField(decimal_places=2, max_digits=15)
	published = models.BooleanField(default=True)
	featured = models.BooleanField(default=True)
	color=models.CharField(max_length=20)

	def __str__(self):
		return self.Product_title



class FeaturedProducts(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1, related_name='featured_products_name')
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='featured_productsuser')
	Product_title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='featured_productscategory')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1, related_name='featured_productssubcategory')	
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	unit = models.CharField(max_length=31, help_text='Unit(e.g Kg, Pc, Etc')
	tags = models.CharField(max_length=30)
	description = RichTextUploadingField()
	price = models.DecimalField(decimal_places=2, max_digits=15)
	available_products = models.CharField(max_length=200)
	image1 = models.ImageField(default='')
	image2 = models.ImageField(null=True, blank=True, default='')
	sale_price = models.DecimalField(decimal_places=2, max_digits=15)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=15)
	shipping_cost = models.DecimalField(decimal_places=2, max_digits=15)
	product_tax = models.DecimalField(decimal_places=2, max_digits=15)
	product_discount = models.DecimalField(decimal_places=2, max_digits=15)
	published = models.BooleanField(default=True)
	featured = models.BooleanField(default=True)
	color=models.CharField(max_length=20)

	def __str__(self):
		return self.Product_title

class ClassifiedAds(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1, related_name='classifiedads_related_name')
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='classifiedadsuser')
	Product_title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='classifiedadscategory')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1, related_name='classifiedadssubcategory')	
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	unit = models.CharField(max_length=30, help_text='Unit(e.g Kg, Pc, Etc')
	tags = models.CharField(max_length=30)
	description = RichTextUploadingField()
	price = models.DecimalField(decimal_places=2, max_digits=15)
	available_products = models.CharField(max_length=200)
	image1 = models.ImageField(default='')
	image2 = models.ImageField(null=True, blank=True, default='')
	sale_price = models.DecimalField(decimal_places=2, max_digits=15)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=15)
	shipping_cost = models.DecimalField(decimal_places=2, max_digits=15)
	product_tax = models.DecimalField(decimal_places=2, max_digits=15)
	product_discount = models.DecimalField(decimal_places=2, max_digits=15)
	published = models.BooleanField(default=True)
	featured = models.BooleanField(default=True)
	color=models.CharField(max_length=20)

	def __str__(self):
		return self.Product_title

