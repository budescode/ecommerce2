from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from .models import ChangePasswordCode, CreateProfie, Vendor
class ChangePasswordCodeAdmin(admin.ModelAdmin):
	fields = ['user_email', 'user_id']
	list_display = ['user_email', 'user_id']
admin.site.register(ChangePasswordCode, ChangePasswordCodeAdmin)
admin.site.register(CreateProfie)
admin.site.register(Vendor)




