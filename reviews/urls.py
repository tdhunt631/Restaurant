from django.conf.urls import patterns, url
from reviews import views

urlpatterns = patterns('',
	url(r'^$', views.Index.as_view(), name="index"),
	url(r'^details/(?P<pk>\d+)/$', views.Details.as_view(), name='details'),
)
