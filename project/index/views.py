from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from administrator.models import Category, SubCategory, VendorPost, Brand, FeaturedProducts, ClassifiedAds
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
	subcategory =SubCategory.objects.all()
	category = Category.objects.all()
	vendor_name = Vendor.objects.all()
	maincategory = Category.objects.get(id=id)
	filter_category = Category.objects.get(id=id)
	qs = VendorPost.objects.filter(category=filter_category)
	details = VendorPost.objects.filter(category=maincategory)
	context = {'category':category, 'subcategory':subcategory, 'qs':qs, 'details':details}
	return render(request, 'category.html', context )

def details(request, id):
	post_pk = request.POST.get("post_pk")
	post = Vendor.objects.get(id_user=post_pk)
	post.delete()
	# print(post.user)
	return JsonResponse({"msg":"deleted"})



def featuredProducts(request):
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	brand = Brand.objects.all()
	featured = FeaturedProducts.objects.all()
	return render(request, 'featuredproducts.html', {'category':category, 'subcategory':subcategory, 'brand':brand, 'featured':featured})

def todays_deal(request):
	return render(request, 'todays_deal.html')

def bundledProducts(request):
	return render(request, 'bundledProducts.html')

def classified_ads(request):
	classified_ads = ClassifiedAds.objects.all()
	return render(request, 'classified_ads.html')

def allbrands(request):
	category = Category.objects.all()
	brand = Brand.objects.all()
	context={'category':category, 'brand':brand}
	return render(request, 'allbrands.html', context)

def allvendors(request):
	return render(request, 'allvendors.html')

def all_vendors_location(request):
	return render(request, 'all_vendors_location.html')

def blog(request):
	return render(request, 'blog.html')

def contact_us(request):
	return render(request, 'contact_us.html')


