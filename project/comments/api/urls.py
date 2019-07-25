from django.urls import path

from django.conf.urls import  url
from .views import (
	CommentCreateAPIVeiw,
	CommentListAPIVeiw,
	# CommentEditAPIView,
	CommentDetailAPIVeiw,
	)

app_name = 'comments'
urlpatterns = [
	
	path('', CommentListAPIVeiw.as_view(), name='list'),
	path('create/', CommentCreateAPIVeiw.as_view(), name='create'),

  path('<int:pk>/',CommentDetailAPIVeiw.as_view(), name='thread'),
  # path('<int:pk>/edit/', CommentEditAPIView.as_view(), name='edit'),
]