from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# Created a query set for the posts
	
	
	return render(request, 'blog/post_list.html',{'posts': posts})
	# request is all the information we get from the user from the internet
	# The second argument dictates which html file we need to include 
	# The third dictionary tries to include the posts from our database into the template file
	