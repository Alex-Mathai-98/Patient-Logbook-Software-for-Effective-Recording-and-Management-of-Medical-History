from django.conf.urls import url
from .import views # importing all our views from the blog application

urlpatterns = [
		url(r'^$',views.post_list,name = 'post_list'),
]

# The first link we have provided is an empty link as per regex rules.
# This is because ==> That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/' is not a part of the URL. 
# This pattern will tell Django that views.post_list is the right place to go if someone enters your website 
# at the 'http://127.0.0.1:8000/' address.

