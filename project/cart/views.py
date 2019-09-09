from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
# Create your views here.
from .models import Cart
from account.models import Vendor

def add_to_cart(request):

	vendor = request.POST.get('vendor')
	# vendor = User.object.get()

	vendoruser = request.POST.get('vendoruser')
	user = User.objects.get(username = vendoruser)
	vendor = Vendor.objects.get(user = user)

	Product_title = request.POST.get('Product_title')
	category = request.POST.get('category')
	subcategory = request.POST.get('subcategory')
	brand = request.POST.get('brand')
	# unit = request.POST.get('unit')
	# tags = request.POST.get('vendor')
	description = request.POST.get('description')
	price = int(request.POST.get('price'))
	image1 = request.POST.get('image1')
	# color=models.CharField(max_length=20, default='')
	quantity = request.POST.get('quantity')
	Cart.objects.create(single_price=price, vendor=vendor, user=request.user, Product_title=Product_title,category=category, subcategory=subcategory, brand=brand, description=description,price=price*quantity, image1=image1,quantity=quantity )
	total_cart = Cart.objects.filter(user=request.user, order=False, paid=False )
	context = {'Product_title':Product_title, 'price':price, 'total_cart':total_cart }	
	return JsonResponse(context)

def cart_checkout(request):
	cart = Cart.objects.filter(user=request.user, paid=False)
	a = 0
	for i in cart:
		a+=i.price
	return render(request, 'cart/cart.html', {'cart':cart, 'total_cart':a})