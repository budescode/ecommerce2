from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from administrator.models import Category, SubCategory, VendorPost, Brand, FeaturedProducts, ClassifiedAds
from account.models import Vendor
from django.db.models import Q



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


def filter_items(request):
	subcategory =SubCategory.objects.all()
	category = Category.objects.all()
	search = request.POST.get('search')
	category1 = request.POST.get('category')
	service = request.POST.get('service')
	if service == 'Vendor':
		searchcategory =  Vendor
		queryset = Vendor.objects.filter( Q(company_name=search) or Q(business_name=search))
	if category1 == 'All Categories':
		queryset = VendorPost.objects.filter( Q(Product_title=search))


	if service == "Products/Services":
		searchcategory = VendorPost
		queryset = VendorPost.objects.filter( Q(Product_title=search) or Q(category=category1))
	
	context = {'category':category, 'subcategory':subcategory, 'queryset':queryset } 
	return render(request, 'filter_search.html', context)
	
def other_filtered_items(request):
	subcategory =SubCategory.objects.all()
	category = Category.objects.all()
	minprice = request.POST.get('minprice')
	maxprice = request.POST.get('maxprice')
	search = request.POST.get('search')
	category1 = request.POST.get('category')
	subcategory1 = request.POST.get('subcategory')
	if category1 == 'ALL CATEGORIES':
		queryset = VendorPost.objects.filter( Q(Product_title=search))
	else:		
		category_qs = Category.objects.get(name=category1)	
		brand1 = request.POST.get('brand')	
		brand_qs = Brand.objects.get(name=brand1)
		subcategory_qs = SubCategory.objects.get(subcategory=subcategory1)
		queryset = VendorPost.objects.filter( Q(Product_title=search) and Q(category=category_qs) and Q(subcategory=subcategory_qs) and Q(brand=brand_qs))
	context = {'queryset':queryset, 'minprice':minprice, 'maxprice':maxprice, 'subcategory':subcategory, 'category':category}
	return render(request, 'other_filtered_products.html', context)

