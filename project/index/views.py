from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from administrator.models import Category, SubCategory, VendorPost, Brand
from account.models import Vendor

def index(request):
	category = Category.objects.all()
	vendor = Vendor.objects.all()
	context={'category':category, 'vendor':vendor}
	return render(request, 'index.html', context)

def allcategories(request):
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	context = {'category':category, 'subcategory':subcategory}
	return render(request, 'allcategories.html', context)

def category(request, id):
	category = Category.objects.all()
	vendor_name = Vendor.objects.all()
	maincategory = Category.objects.get(id=id)
	qs = VendorPost.objects.filter(category=category)
	details = VendorPost.objects.filter(category=maincategory)
	context = {'category':category, 'subcategory':'subcategory', 'qs':qs, 'details':details}
	return render(request, 'category.html', context )

def details(request, id):
	post_pk = request.POST.get("post_pk")
	post = Vendor.objects.get(id_user=post_pk)
	post.delete()
	# print(post.user)
	return JsonResponse({"msg":"deleted"})