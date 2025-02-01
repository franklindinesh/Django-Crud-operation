from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name','email','field_of_study','gpa']
		labels = {
			'first_name':'First_name',
			'last_name':'Last_name',
			'email':'Email',
			'field_of_study':'Field_of_study',
			'gpa':'CGPA'
		}

		widgets = {
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
			'gpa':forms.NumberInput(attrs={'class':'form-control'})

		}