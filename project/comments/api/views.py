from django.db.models import Q

# This in bult functions for search
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)
# importing paginations
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import PostLimitOffsetPagination

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

from comments.models import Comment

from .serializers import (
	CommentSerializer,
	CommentDetailSerializer
	)


# class PostCreateAPIVeiw(CreateAPIView):
# 	"""
# 	Create Content
# 	"""
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	permissions_classes = [IsAuthenticated]

# 	# It changes to the user who create content to new user.
# 	def perform_create(self, serializer):
# 		serializer.save(user=self.request.user)



class CommentDetailAPIVeiw(RetrieveAPIView):
	"""
	Retrieve a specific Content by ID
	"""
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer
	lookup_field = 'pk'

# class PostUpdateAPIVeiw(RetrieveUpdateAPIView):
# 	"""
# 	Update Content By a slug or ID
# 	"""
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateUpdateSerializer
# 	lookup_field = 'slug'
# 	permissions_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# 	# create user Permissions
# 	def perform_update(self, serializer):
# 		serializer.save(user=self.request.user)


# class PostDeleteAPIVeiw(DestroyAPIView):
# 	"""
# 	Delete Content By a slug or ID
# 	"""
# 	queryset = Post.objects.all()
# 	serializer_class = PostDetailSerializer
# 	lookup_field = 'slug'


class CommentListAPIVeiw(ListAPIView):
	"""
	Retrivew all the Content
	"""
	serializer_class = CommentSerializer

	# You pass things to search
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['content', 'user_first_name']
	# Pagination
	pagination_class = PostLimitOffsetPagination


	def get_queryset(self, *args, **kwargs):
		# querset_list = super(PostListAPIVeiw, self).get_queryset(*args, **kwargs)
		querySet_list = Comment.objects.all()
		query = self.request.GET.get("q")
		if query:
			querySet_list = querySet_list.filter(
								Q(content__icontains=query)|
								Q(user__username__icontains=query)
								).distinct()
		return querySet_list

