from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	CreateAPIView,
	)

from posts.models import Post
from .serializers import (
	PostDetailSerializer,
	PostListSerializer,
	PostCreateUpdateSerializer,
	)


class PostCreateAPIVeiw(CreateAPIView):
	"""
	Create Content
	"""
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer



class PostDetailAPIVeiw(RetrieveAPIView):
	"""
	Retrieve a specific Content by ID
	"""
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIVeiw(UpdateAPIView):
	"""
	Update Content By a slug or ID
	"""
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'


class PostDeleteAPIVeiw(DestroyAPIView):
	"""
	Delete Content By a slug or ID
	"""
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostListAPIVeiw(ListAPIView):
	"""
	Retrivew all the Content
	"""
	queryset = Post.objects.all()
	serializer_class = PostListSerializer


