# import the standard Django Model 
# from built-in library 
from django.db import models 

# declare a new model with a name "GeeksModel" 
class SampleModel(models.Model): 

	# fields of the model 
	title = models.CharField(max_length = 200) 

	# renames the instances of the model 
	# with their title name 
	def __str__(self): 
		return self.title 
