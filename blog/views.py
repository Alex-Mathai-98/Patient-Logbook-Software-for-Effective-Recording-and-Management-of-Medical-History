from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.

def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# Created a query set for the posts

	return render(request, 'blog/post_list.html',{'posts': posts})
	# request is all the information we get from the user from the internet
	# The second argument dictates which html file we need to include 
	# The third dictionary tries to include the posts from our database into the template file
	
def post_detail(request,pk):
	post = get_object_or_404(Post,pk = pk)
	return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
	if(request.method == "POST"): 
		#In the html file we have named the method as "POST". Remember this must not be named something else. 
		#If the method is equal to POST, then that means that the file has been filled in once. Or in another sense
		#the button has been accessed once and information has been "posted once" 
		#all the information is in the post method and we want to create a form with all that information
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False) #we don't want to save the form until we add the author and published date, hence commit is false 
			post.author = request.user
			post.published_date = timezone.now()
			post.save() # now everything is saved
			return redirect('post_detail',pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request,pk):
	post = get_object_or_404(Post,pk = pk) #Just writing pk will not work, because pk is a variable. you need to write pk = pk!
	if request.method == "POST":
		form = PostForm(request.POST,instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail',pk = post.pk)
	else:
			form = PostForm(instance = post)
	return render(request,'blog/post_edit.html',{'form':form})

