from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField

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

post_detail_url = HyperlinkedIdentityField(

	view_name='posts-api:detail',
	lookup_field='slug'
)

class PostListSerializer(ModelSerializer):
	"""
	Retrivew all the Content
	"""
	url = post_detail_url
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'publish'
		]

class PostDetailSerializer(ModelSerializer):
	"""
	Retrieve a specific Content by ID
	"""
	url = post_detail_url
	class Meta:
		model = Post
		fields = [
			'url',
			'id',
			'title',
			'slug',
			'content',
			'publish'
		]
