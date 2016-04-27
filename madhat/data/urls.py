from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^sales/$', views.Sales),
	url(r'^sales/(?P<id>[0-9]+)/$', views.SalesDetail),
]