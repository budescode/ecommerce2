from django.db import models
from django.contrib.auth.models import User

import uuid
class PasswordResetEmail(models.Model):
	email = models.EmailField()
class ChangePasswordCode(models.Model):
	user_email = models.EmailField(max_length=50)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
class ChangePassword(models.Model):
	new_password = models.CharField(max_length=50, blank = False, null = False)
	confirm_new_password = models.CharField(max_length=50, blank = False, null = False)

class CreateProfie(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
	username = models.CharField(max_length=100)
	email = models.EmailField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.IntegerField()
	address_line_1 = models.CharField(max_length=200)
	address_line_2 = models.CharField(max_length=200, blank=True, null=True)
	state = models.CharField(max_length=40)
	country = models.CharField(max_length=40)
	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Vendor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='vendor_user')
	company_name = models.CharField(max_length=100)
	business_name = models.CharField(max_length=100, help_text='Registered business name')
	logo = models.ImageField(default='default.jpg')
	banner = models.ImageField(default='default.jpg')
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.company_name