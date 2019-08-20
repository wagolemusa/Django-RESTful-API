from django.urls import path

from django.conf.urls import  url
from .views import (
	PostCreateAPIVeiw,
	PostDetailAPIVeiw,
	PostListAPIVeiw,
	PostUpdateAPIVeiw,
	PostDeleteAPIVeiw
	# post_list,
	# post_create,
	# post_detail,
	# post_update,
	# post_delete,
	)

app_name = 'posts'
urlpatterns = [

  path('',  PostListAPIVeiw.as_view(), name='list'),
  path('create/', PostCreateAPIVeiw.as_view(), name='create'),
  path('<slug:slug>/',PostDetailAPIVeiw.as_view(), name='detail'),
  path('<slug:slug>/edit/', PostUpdateAPIVeiw.as_view(), name='update'),
  path('<slug:slug>/delete/', PostDeleteAPIVeiw.as_view(), name='delete'),
]