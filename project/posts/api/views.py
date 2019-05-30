from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	)

from posts.models import Post
from .serializers import PostDetailSerializer, PostListSerializer

class PostDetailAPIVeiw(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIVeiw(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostDeleteAPIVeiw(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostListAPIVeiw(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer


