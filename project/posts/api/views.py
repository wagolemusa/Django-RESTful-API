from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView
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

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)



class PostDetailAPIVeiw(RetrieveAPIView):
	"""
	Retrieve a specific Content by ID
	"""
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIVeiw(RetrieveUpdateAPIView):
	"""
	Update Content By a slug or ID
	"""
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


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


