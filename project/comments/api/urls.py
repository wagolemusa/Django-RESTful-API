from django.urls import path

from django.conf.urls import  url
from .views import (
	CommentListAPIVeiw,
	CommentDetailAPIVeiw,
	)

app_name = 'comments'
urlpatterns = [
	
	path('', CommentListAPIVeiw.as_view(), name='list'),
  path('<int:id>/',CommentDetailAPIVeiw.as_view(), name='thread'),
  # path('<int:id>/delete/', comment_delete, name='delete'),
]