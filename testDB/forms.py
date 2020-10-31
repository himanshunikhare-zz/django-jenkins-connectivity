from django import forms
from django.db.models import fields 
from .models import SampleModel 
from django.forms import ModelForm


# creating a form 
class SampleForm(ModelForm): 
	
	class Meta:
		model = SampleModel
		fields = '__all__'