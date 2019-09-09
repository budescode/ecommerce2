from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
from django.urls import path


app_name = "index"
urlpatterns = [
	path('', views.index, name='index'),
	path('allcategories/', views.allcategories, name='allcategories'),
	path('category/<slug:id>/', views.category, name='category'),
	path('featured-products/', views.featuredProducts, name='featuredProducts'),
	path('todays-deal/', views.todays_deal, name='todays_deal'),
	path('bundled-products/', views.bundledProducts, name='bundledProducts'),
	path('classified-ads/', views.classified_ads, name='classified_ads'),
	path('allbrands/', views.allbrands, name='allbrands'),
	path('allvendors/', views.allvendors, name='allvendors'),
	path('all-vendors-location/', views.all_vendors_location, name='all_vendors_location'),
	path('blog/', views.blog, name='blog'),
	path('contact-us/', views.contact_us, name='contact_us'),








]
