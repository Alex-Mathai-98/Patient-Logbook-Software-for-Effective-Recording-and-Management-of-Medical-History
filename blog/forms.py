from .models import Post
from django import forms
''' The class Meta tells what models needs to be used, i.e. in this case Post, the fields statement is simple!, Author is 
the person who is currently logged in and the created date is automatic according to the code'''


class PostForm(forms.ModelForm):

	# the meta class is used for telling django which model must be used to create the form
	class Meta:
		model = Post # the name of the model in our models.py file
		fields = ('title','text',)  # the fields we want in our form, dates will automatically be created due to default option