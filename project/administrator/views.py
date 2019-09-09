from django.shortcuts import render, redirect
from .forms import VendorPostForm
from django.http import HttpResponseRedirect, HttpResponse 
from .models import VendorPost, Brand, SubCategory, Category
from account.models import Vendor
from django.contrib.auth.decorators import login_required
from account.forms import EditVendorImage


@login_required(login_url='/account/login/')
def administrator(request):
	return render(request, 'administrator/index.html')

@login_required(login_url='/account/login/')
def products(request):
	qs = VendorPost.objects.filter(user = request.user)
	context = {'qs':qs}
	return render(request, 'administrator/products.html', context)

@login_required(login_url='/account/login/')
def add(request):
	try:		
		category = Category.objects.all()
		subcategory = SubCategory.objects.all()
		brand = Brand.objects.all()
		vendor = Vendor.objects.get(user=request.user)
		if request.method=='POST':
			form = VendorPostForm(request.POST or None, request.FILES or None)
			if form.is_valid():				
				
				# if form.is_valid():
				data = form.save(commit=False)
				data.user  = request.user
				data.vendor = vendor
				data.save()
				return redirect('administrator:products')
		else:
			form=VendorPostForm()
		context = {'form':form, 'category':category, 'subcategory':subcategory, 'brand':brand}
		return render(request, 'administrator/add.html', context)
	except Vendor.DoesNotExist:
		return HttpResponse('you"re not a registered vendor')


@login_required(login_url='/account/login/')
def delete(request, id):
	qs = VendorPost.objects.get(id=id, user=request.user)
	qs.delete()
	return redirect('administrator:products')


@login_required(login_url='/account/login/')
def edit(request, id):
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	brand = Brand.objects.all()
	data = VendorPost.objects.get(id=id, user=request.user)
	if request.method=='POST':
		
		form = VendorPostForm(request.POST or None, request.FILES or None, instance = data)
		if form.is_valid():				
			
			# if form.is_valid():
			data = form.save(commit=False)
			data.user  = request.user
			data.save()
			return redirect('administrator:products')
	else:
		form=VendorPostForm(instance = data)
	context = {'form':form, 'category':category, 'subcategory':subcategory, 'brand':brand}
	return render(request, 'administrator/edit.html', context)


@login_required(login_url='/account/login/')
def details(request, id):
	qs = VendorPost.objects.get(id=id)
	context={'qs':qs}
	return render(request, 'administrator/details.html', context)

@login_required(login_url='/account/login/')
def settings(request):
	vendor1 = Vendor.objects.get(user=request.user)
	if request.method == 'POST':
		form = EditVendorImage(request.POST or None, request.FILES or None)
		if form.is_valid():
			banner = form.cleaned_data.get('banner')
			logo = form.cleaned_data.get('logo')
			vendor.logo = logo
			vendor.banner = banner
			vendor.save()
			return redirect('administrator:settings')
	else:
		form = EditVendorImage()
		
	context = {'form':form, 'vendor1':vendor1}

	return render(request, 'administrator/settings.html', context)