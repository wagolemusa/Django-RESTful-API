from django.db.models import Q
from django.contrib.auth import get_user_model

# This in bult functions for search
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)
# importing paginations
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import PostLimitOffsetPagination

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
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

User = get_user_model()


from .serializers import (
	UserCreateSerializer
	)

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
