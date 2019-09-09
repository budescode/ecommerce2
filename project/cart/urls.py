from django.conf.urls import url, include

from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views




from django.urls import path


app_name = "cart"
urlpatterns = [
	path('', views.add_to_cart, name='add_to_cart'),
	path('cart-checkout/', views.cart_checkout, name='cart_checkout'),






]


