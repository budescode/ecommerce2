from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order
from cart.models import Cart

def create_order(request):
	cart1 = Cart.objects.filter(user=request.user, paid=False, order=False)
	email = request.POST.get('email')
	phone_number = request.POST.get('phone_number')
	address_line_1 = request.POST.get('address_line_1')
	address_line_2 = request.POST.get('address_line_2')
	last_name = request.POST.get('last_name')
	first_name = request.POST.get('first_name')
	user = User.objects.get(username = request.user.username)
	for i in cart1:
		order = Order.objects.create(vendor = i.vendor, cart=i,user=user,email=email, phone_number=phone_number, address1=address_line_1, address2=address_line_2, first_name=first_name, last_name=last_name,payment_method='payment on delivery')
		i.order = True
		i.save()



		# cart1 = Cart.objects.get(pk=i.pk)
		# cart1.order = True
		# cart1.save()
		# print(cart1.order)
		
	return render(request, 'order/order.html')