from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
<<<<<<< HEAD
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,

=======
    RetweetView,
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
    TweetListView,
    TweetUpdateView
    )

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
<<<<<<< HEAD
=======
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='detail'), # /tweet/1/
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]

