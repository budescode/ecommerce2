from django.conf.urls import url, include

from . import views





from django.urls import path


app_name = "order"
urlpatterns = [
	path('create_order/', views.create_order, name='create_order'),







]

