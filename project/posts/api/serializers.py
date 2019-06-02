from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
	"""
	Create Contents
	"""
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'publish'
		]

class PostListSerializer(ModelSerializer):
	"""
	Retrivew all the Content
	"""
	class Meta:
		model = Post
		fields = [
			'user',
			'title',
			'slug',
			'content',
			'publish'
		]

class PostDetailSerializer(ModelSerializer):
	"""
	Retrieve a specific Content by ID
	"""
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'publish'
		]
