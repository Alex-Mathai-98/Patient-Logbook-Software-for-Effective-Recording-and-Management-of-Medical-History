from django.shortcuts import render,get_object_or_404,redirect
from .models import Patient,Family,Patient_List
from .forms import Patient_New_Form 
from django.db.models import Q
from django.views.generic import ListView,DeleteView
import operator
import functools
from django.urls import reverse_lazy

# Create your views here.

def patient_detail(request, pk):
	primary_key = pk
	current_patient = get_object_or_404(Patient,pk = primary_key)
	family = current_patient.Family

	# Finding the total family balance
	family_members = family.patient_set.all()
	total_balance = 0
	for member in family_members:
		total_balance += member.Pending_Balance   

	current_patient.Family_Balance = total_balance
	current_patient.save()

	return render(request,'patient/patient_detail.html', {'current_patient': current_patient,'family':family})

# This is done!!
def create_patient(request):
	if(request.method == "POST"):
		form = Patient_New_Form(request.POST)
		if form.is_valid:
			new_patient = form.save(commit = False)
			new_patient.Family_Id_Display = new_patient.Family.Family_Id_Number  

			# I have already EXACTLY ONE Patient_List object called the "Master List" 
			Patient_List_temp,create = Patient_List.objects.get_or_create(Name ="Master List")
			new_patient.Patient_List = Patient_List_temp

			family_members = new_patient.Family.patient_set.all()
			if(len(family_members) != 0):
				total_balance = 0
				for member in family_members:
					total_balance += member.Pending_Balance  
				new_patient.Family_Balance = total_balance
			else:
				new_patient.Family_Balance = new_patient.Pending_Balance	

			new_patient.save()

			return redirect('patient_detail',pk = new_patient.Patient_Id)
	else:
		form = Patient_New_Form()

	return render(request,'patient/create_patient.html',{'form':form})

def patient_center_home(request):
	return render(request,'patient/patient_center_home.html')

MIN_SEARCH_CHARS = 2
''' Trying to fix the least number of characters required for searching in the website'''

def search_patient(request):
	return render(request,'patient/search_patient.html',)

class patient_list(ListView):
	''' Displays all the patients related to the search results'''

	model = Patient
	context_object_name = "patients"
	template_name = "patient/patient_list.html"

	def dispatch(self,request,*args,**kwargs):
		self.request = request #So get_context_data can access the request variable
		return super(patient_list,self).dispatch(request,*args,**kwargs)

	def get_queryset(self):
		''' Returns all the patients for display in the main website '''
		return super(patient_list,self).get_queryset()

	def get_context_data(self,**kwargs):

		# The current context
		context = super(patient_list,self).get_context_data(**kwargs)

		global MIN_SEARCH_CHARS

		# Assume that there is no search
		search_text = ""

		# the request must be GET and not POST. Also not if(self.request.GET). This won't work!
		if(self.request.method == "GET"):
			search_text = self.request.GET.get("search_text"," ").strip()

			if(len(search_text) < MIN_SEARCH_CHARS):
				# Ignore Search
				search_text = " "

		if(search_text != " "):
			# Taking out leading and trailing whitespaces and splitting the search in words
			search_text_list = search_text.strip().split()
			# operator.or_ wraps an "or" option around the arguments for the filter, similarly operator.and_ wraps an "and" option around the argumnets for the filter
			# the reduce function is basically defined as the following.
			# reduce(func,list):
			#	result = list.pop() --- get the last element of the list
			#	for item in list:
			#		result = func(result,item) --- depending on the function,it will perform operation.In this case it is adding an "OR" between the items 
			search_text_results = Patient.objects.filter(
				functools.reduce(operator.or_,
					(Q(First_Name__icontains = word) for word in search_text_list)) |
				functools.reduce(operator.or_,
					(Q(Middle_Name__icontains = word) for word in search_text_list)) |
				functools.reduce(operator.or_,
					(Q(Last_Name__icontains = word) for word in search_text_list)),)

			

		else :
			#An empty list instead of None. In the template, use
            #{% if color_search_results.count > 0 %}
			search_text_results = []

		# Creating a context dictionary with all information needed
		context['search_text'] = search_text
		context['search_text_results'] = search_text_results
		context['MIN_SEARCH_CHARS'] = MIN_SEARCH_CHARS

		return context

def patient_edit(request,pk):
	patient = get_object_or_404(Patient,pk = pk) #Just writing pk will not work, because pk is a variable. you need to write pk = pk!
	if request.method == "POST":
		form = Patient_New_Form(request.POST,instance = patient)
		if form.is_valid():
			patient = form.save()
			return redirect('patient_detail',pk = patient.pk)
	else:
			form = Patient_New_Form(instance = patient)
	return render(request,'patient/patient_edit.html',{'form':form})

class patient_delete(DeleteView):
	model = Patient
	template_name = "patient/patient_delete_confirm_delete.html"
	success_url = reverse_lazy('patient_list')
	



