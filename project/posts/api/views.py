from rest_framework.generics import ListAPIView

from posts.models import Post

class PostListAPIVeiw(ListAPIView):
	queryset = Post.objects.all()