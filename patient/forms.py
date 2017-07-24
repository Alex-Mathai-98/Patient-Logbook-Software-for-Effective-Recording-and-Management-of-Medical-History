from django import forms
from .models import Patient,Family

class Patient_New_Form(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('Title','First_Name','Middle_Name','Last_Name','Gender','Family','Birth_Date','Blood_Group','Mobile1','Mobile2','Pending_Balance','Last_Pay_Date',)
	# You need to make sure to only validate the fields that are present in the form, All other fields should be dealt with the views method function later
	# Form fields do not have a blank option, they oonly have the required option. Putting a blank option will not work	
	New_Family = forms.CharField(max_length=100,required = False,help_text = "Put in your family name here only if your family name has not been saved before", label = 'New Family')
	New_Family_Address = forms.CharField(max_length = 100,required = False,help_text = "Address")
	New_Family_Area = forms.CharField(max_length = 100,required = False,help_text = "Area")
	New_Family_City = forms.CharField(max_length = 100,required = False,help_text = "City")
	New_Family_Pincode = forms.IntegerField(required = False, help_text = "Pincode")
	New_Family_State = forms.CharField(max_length = 100,required = False, help_text = "State")
	field_order = ['Title','Family','Gender','First_Name','Middle_Name','Last_Name','Birth_Date','Blood_Group','Pending_Balance','Mobile1','Mobile2','Last_Pay_Date','New_Family','New_Family_Address','New_Family_Area','New_Family_City','New_Family_State','New_Family_Pincode']

	def __init__(self,*args,**kwargs):
		super(Patient_New_Form,self).__init__(*args,**kwargs)
		self.fields['Family'].required = False
	#This over-rides the base class clean definiton,hence we need to call the base class clean method atleaset once.
	#Avoid putting such logic in views. Just put it in the form itself. Because relation creating occurs during form initialization and form validation itself.
	# 
	def clean(self):
		#CLEANED DATA IS ALREADY PREPARED WHEN CALLING THE IS_VALID METHOD
		# Remember you must only use ' ' AND NOT " " in the get function 
		Form_Family = self.cleaned_data.get('Family')
		New_Family = self.cleaned_data.get('New_Family')
		New_Family_Address = self.cleaned_data.get('New_Family_Address')
		New_Family_Area = self.cleaned_data.get('New_Family_Area')
		New_Family_City = self.cleaned_data.get('New_Family_City')
		New_Family_Pincode = self.cleaned_data.get('New_Family_Pincode')
		New_Family_State = self.cleaned_data.get('New_Family_State')

		if not Form_Family and not New_Family:
			raise forms.ValidationError("Please select an already existing family OR enter a new family,NOT BOTH!")
		elif not Form_Family and New_Family:
			new_object,created = Family.objects.get_or_create(Family_Name = New_Family,Address = New_Family_Address,Area = New_Family_Area,City = New_Family_City,Pincode = New_Family_Pincode,State = New_Family_State)
			if(not created): # checking if a new family is created
				self.cleaned_data['Family'] = new_object
			else:
				self.cleaned_data['Family'] = New_Family
				# EVEN IF THE USER INPUTS AN ALREADY EXISTING FAMILY, IT WILL REGITER THE OLD FAMILY THAT IS ALREADY SAVED
		return super(Patient_New_Form,self).clean()





		