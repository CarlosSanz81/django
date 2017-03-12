from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hola_mundo, name='hola'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
	url(r'^product/new', views.new_product, name='nuevo_producto'),
]

    