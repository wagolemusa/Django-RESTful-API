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
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer



class PostDetailAPIVeiw(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIVeiw(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'


class PostDeleteAPIVeiw(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostListAPIVeiw(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer


