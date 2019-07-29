from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
	CharField,
	EmailField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError
	)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
	email = EmailField(label = 'Email Address')
	email2 = EmailField(label='Confirm Email')
	class Meta:
		model = User 
		fields = [
			'username',
			'email',
			'email2',
			'password',
		]
		extra_kwargs = {"password":
											{"write_only": True}
										}

	# Compare Email address if they exists.
	def validete(self, data):
		# email = data['email']
		# user_qs = User.object.filter(email=email)
		# if user_qs.exists():
		# 	raise ValidationError("This Email Address is already registered")
		return data

	# Validates Emails 
	def validate_email2(self, value):
		data = self.get_initial()
		email1 = data.get("email")
		email2 = value
		if email1 != email2:
			raise ValidationError("Emails must match")

		# Compare Email address if they exists.
		user_qs = User.objects.filter(email=email2)
		if user_qs.exists():
			raise ValidationError("This Email Address is already registered")
		return value
										
	# Save a user in the model
	def create(self, validate_data):
		username = validate_data['username']
		email = validate_data['email']
		password = validate_data['password']

		user_obj = User(

				username = username,
				email = email
			)
		user_obj.set_password(password)
		user_obj.save()
		return validate_data

class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField() 
	email = EmailField(label = 'Email Address')
	class Meta:
		model = User 
		fields = [
			'username',
			'email',
			'password',
			'token',
		]
		extra_kwargs = {"password":
											{"write_only": True}
										}

	# Compare Email address if they exists.
	def validete(self, data):
		# email = data['email']
		# user_qs = User.object.filter(email=email)
		# if user_qs.exists():
		# 	raise ValidationError("This Email Address is already registered")
		return data