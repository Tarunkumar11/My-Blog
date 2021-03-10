
from django.conf.urls import url
from blog import views
from . import forms
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from blog.views import HomeView
urlpatterns = [
    url(r'^$',HomeView.as_view(),name = 'home'),
    url(r'^about/',views.AboutView.as_view(),name = 'about'),
    url(r'Signup/$',views.Signup.as_view(),name = 'signup'),
    url(r'^logout',views.LogOutView.as_view(),name='logout'),
    url(r'^contact',views.AddQueryForm,name='contact'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
