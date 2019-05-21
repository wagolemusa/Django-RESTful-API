from django import forms

from .models import Post
from pagedown.widgets import PagedownWidget

class PostForms(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(label = '', widget=forms.SelectDateWidget)

	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish",

		]