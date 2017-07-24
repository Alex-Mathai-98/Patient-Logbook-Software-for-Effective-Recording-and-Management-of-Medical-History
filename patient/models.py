from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here
class Operation(models.Model):
	Operation_Description = models.TextField()
	Operation_Cost = models.IntegerField()
	Day_of_Operation = models.DateTimeField()

class Family(models.Model):
	Family_Id_Number = models.AutoField(primary_key = True)  
	Family_Name = models.CharField(max_length = 100,default = " ", blank = True)
	Address = models.CharField(default = " ",max_length = 100,blank = True)
	Area = models.CharField(max_length = 100,blank = True,default = " ")
	City = models.CharField(max_length = 100,blank = True,default = " ")
	Pincode = models.IntegerField(blank = True,default = 0)
	State = models.CharField(max_length = 100, blank = True, default = " ")

	def __str__(self):
		return self.Family_Name + " #" + str(self.Family_Id_Number)

TITLE_CHOICES = (
	('Mr', 'Mr'),
	('Mrs', 'Mrs'),
	('Miss','Miss'),
	('Master','Master'),
	)

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	)
BLOOD_CHOICES = (
	('A+','A+'),
	('B+','B+'),
	('O+','O+'),
	('A-','A-'),
	('B-','B-'),
	('O-','O-'),
	)

class Patient_List(models.Model):
	Name = models.CharField(null = True, max_length = 20, blank = True)
	

class Patient(models.Model):
	Title = models.CharField(choices = TITLE_CHOICES,max_length = 6)
	Family = models.ForeignKey(Family) # Multiple patients connected to a single family 
	Family_Id_Display = models.IntegerField(blank = True,null = True) ### Found out in views.py file
	Patient_List = models.ForeignKey(Patient_List) # The record that contains all the patients
	Patient_Id = models.AutoField(primary_key = True) # Added by Default
	First_Name = models.CharField(max_length = 100,blank = False,verbose_name = 'First Name')
	Middle_Name = models.CharField(max_length = 100,blank = True)
	Last_Name = models.CharField(max_length = 100,blank = True)
	Gender = models.CharField(choices = GENDER_CHOICES,max_length = 1)
	Birth_Date = models.DateTimeField(blank = True,null = True)
	Blood_Group = models.CharField(choices = BLOOD_CHOICES,max_length = 2,blank = True)
	Mobile1 = models.IntegerField(validators = [MinValueValidator(1000000000),MaxValueValidator(9999999999)])
	Mobile2 = models.IntegerField(validators = [MinValueValidator(1000000000),MaxValueValidator(9999999999)])
	Pending_Balance = models.IntegerField(blank = True)
	Family_Balance = models.IntegerField(blank = True,default = 0)
	Last_Pay_Date = models.DateTimeField(blank = True,null = True) ### Improve this!

	def add_operation(self,Operation):
		self.Operation_List.add(Operation)
		self.save()

	def __str__(self):
		return (self.First_Name + ' ' + self.Middle_Name + ' ' + self.Last_Name) 



