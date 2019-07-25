from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError
	)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
	class Meta:
		model = User 
		fields = [
			'username',
			'email',
			'password',
		]
		extra_kwargs = {"password":
											{"write_only": True}
										}
										
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