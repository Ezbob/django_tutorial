from django.conf.urls import url

from . import views
from .views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	#  /polls/5/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	#  /polls/5/results
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
