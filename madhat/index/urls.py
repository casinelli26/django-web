from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.Welcome),
	url(r'^home/$', views.Home),
    url(r'^about/$', views.About),
    url(r'^logout/$', views.Logout),
    url(r'^test/$', views.Test),
]