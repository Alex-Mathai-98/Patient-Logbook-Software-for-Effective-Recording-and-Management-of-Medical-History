from django.conf.urls import url,include
from . import views

urlpatterns = [
	#main page of the website
	url(r'^centerhome/$',views.patient_center_home, name ="patient_center_home"),

	#details of a patient
	url(r'^(?P<pk>\d+)/detail/$',views.patient_detail,name ='patient_detail'),

	#creating a patient
	url(r'^create/$',views.create_patient,name ="create_patient"),

	#searching a patient
	url(r'^search/$',views.search_patient,name="search_patient"),

	#displaying the search results
	url(r'^list/$',views.patient_list.as_view(),name="patient_list"),

	#edit an already existing patient
	url(r'^(?P<pk>\d+)/edit/$',views.patient_edit,name = "patient_edit"),

	# Deleting a patient using the DeleteView Class
	# Very important to include the (?P<pk>\d+) in the url itself, because the get_object method will take the information from the URL
	url(r'^(?P<pk>\d+)/delete/$',views.patient_delete.as_view(),name = "patient_delete"),
]