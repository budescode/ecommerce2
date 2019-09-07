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






]
