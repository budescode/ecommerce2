from django.shortcuts import render, redirect
from .forms import VendorPostForm
from django.http import HttpResponseRedirect, HttpResponse 
from .models import VendorPost
from account.models import Vendor

# Create your views here.
def administrator(request):
	return render(request, 'administrator/index.html')

def products(request):
	qs = VendorPost.objects.filter(user = request.user)
	context = {'qs':qs}
	return render(request, 'administrator/products.html', context)
def add(request):
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
	context = {'form':form}
	return render(request, 'administrator/add.html', context)

def delete(request, id):
	qs = VendorPost.objects.get(id=id, user=request.user)
	qs.delete()
	return redirect('administrator:products')

def edit(request, id):
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
	context = {'form':form}
	return render(request, 'administrator/edit.html', context)

def details(request, id):
	qs = VendorPost.objects.get(id=id)
	context={'qs':qs}
	return render(request, 'administrator/details.html', context)