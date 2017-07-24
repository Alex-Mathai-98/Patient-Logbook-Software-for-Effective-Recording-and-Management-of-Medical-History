"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView

from blog import views as blog_views
# the r of the pattern denotes that this is a regular expression to python
# Django will now redirect everything that comes into 'http://127.0.0.1:8000/' to blog.urls and look for further instructions there.

# the include function chops off the url till the '/' symbol. i.e. If you want services/common_services it will chop the "services/" part
# and pass the rest "common_services to the services/urls.py file" . Always use include, except when it comes to the admin part
# then use only admin.site.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls'),{'blog': "blog"}),
    url(r'^patient/',include('patient.urls')),
    #url(r'^$/',include('services.urls'))
    url(r'^hola/$',TemplateView.as_view(template_name='hi.html')),
    url(r'^$', blog_views.post_list),
]
