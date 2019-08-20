from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from accounts.api.serializers import UserDetailSerializer

# imports from comments in api
from comments.api.serializers import CommentSerializer
from comments.models import Comment
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
	Retrieve a specific Content by ID
	"""
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'publish',
		]
	def get_user(self, obj):
		return str(obj.user.username)

class PostDetailSerializer(ModelSerializer):
	"""
	Retrivew all the Content
	"""
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()
	html =  SerializerMethodField()
	read  = SerializerMethodField()
	comments = SerializerMethodField()

	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'html',
			'read',
			'publish',
			'image',
			'comments',
		]

	def get_read(self, obj):
		return obj.read_time

	def get_html(self, obj):
		return obj.get_markdown()

	def get_user(self, obj):
		return str(obj.user.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image 

	def get_comments(self, obj):
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(c_qs, many=True).data
		return comments
