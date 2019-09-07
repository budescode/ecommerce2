from cart.models import Cart
def cartContextProcessors(request):
	a = 0
	cart_count = Cart.objects.filter(user=request.user, paid=False).count()
	cart = Cart.objects.filter(user=request.user, paid=False)
	for i in cart:
		a = a + (int(i.price) * int(i.quantity))
	return {'contextcart_count': cart_count, 'contextcart':cart, 'contextcart_price':a}