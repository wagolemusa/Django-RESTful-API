from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

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


class PostDetailSerializer(ModelSerializer):
	"""
	Retrieve a specific Content by ID
	"""
	url = post_detail_url
	user = SerializerMethodField()
	image = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'url',
			'id',
			'user',
			'title',
			'slug',
			'content',
			'publish',
			'image',
		]
	def get_user(self, obj):
		return str(obj.user.username)

class PostListSerializer(ModelSerializer):
	"""
	Retrivew all the Content
	"""
	url = post_detail_url
	user = SerializerMethodField()
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
