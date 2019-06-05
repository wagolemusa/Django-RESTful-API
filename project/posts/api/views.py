from django.db.models import Q

# This in bult functions for search
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView
	)

# To import user Permissions in Django apis
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly

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
	permissions_classes = [IsAuthenticated]

	# It changes to the user who create content to new user.
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
	permissions_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	# create user Permissions
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
	serializer_class = PostListSerializer

	# You pass things to search
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'content', 'user_first_name']


	def get_queryset(self, *args, **kwargs):
		# querset_list = super(PostListAPIVeiw, self).get_queryset(*args, **kwargs)
		querySet_list = Post.objects.all()
		query = self.request.GET.get("q")
		if query:
			querySet_list = querySet_list.filter(
								Q(title__icontains=query)|
								Q(content__icontains=query)|
								Q(user__username__icontains=query)
								).distinct()
		return querySet_list

