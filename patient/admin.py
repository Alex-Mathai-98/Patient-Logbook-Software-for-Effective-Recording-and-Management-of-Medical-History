from django.contrib import admin
from .models import Patient,Patient_List,Family
# Register your models here.

admin.site.register(Patient)
admin.site.register(Patient_List)
admin.site.register(Family)