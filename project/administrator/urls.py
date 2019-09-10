from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views



from django.contrib.auth.views import PasswordResetView

from django.urls import path


app_name = "administrator"
urlpatterns = [
	path('', views.administrator, name='administrator'),
	path('products/', views.products, name='products'),
	path('add/', views.add, name='add'),
	path('delete/<slug:id>/', views.delete, name='delete'),
	path('edit/<slug:id>/', views.edit, name='edit'),
	path('details/<slug:id>/', views.details, name='details'),
	path('settings/', views.settings, name='settings'),
	path('sale/', views.sale, name='sale'),






]







