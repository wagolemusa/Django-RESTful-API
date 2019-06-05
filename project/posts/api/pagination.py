# This ins in bult function for pPagination

from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination,
	)


class PostLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 2
	max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
	page_sze = 2
