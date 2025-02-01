from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm

# "GET" is used to retrieve data from a server, 
# "POST" is used to create new data, 
# "PUT" is used to fully update an existing resource
# "DELETE" is used to remove a resource from the server.

# Create your views here.

def index(request):
	return render(request,"pages/index.html",{
		'students': Student.objects.all()
		})



def view_student(request, id):
	student = Student.object.get(pk=id)
	return HttpResponseRedirect(reverse('index'))

def add(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			new_first_name = form.cleaned_data['first_name']
			new_last_name = form.cleaned_data['last_name']
			new_email = form.cleaned_data['email']
			new_field_of_study = form.cleaned_data['field_of_study']
			new_gpa = form.cleaned_data['gpa']

			new_student = Student(
					first_name = new_first_name,
					last_name = new_last_name,
					email = new_email,
					field_of_study = new_field_of_study,
					gpa = new_gpa
				)
			new_student.save()
			return render(request, 'pages/add.html',{
				'form':StudentForm(),
				'success':True
				})

	else:
		form = 	StudentForm()
	return render(request, 'pages/add.html',{
		'form':StudentForm()
	})	

def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'pages/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'pages/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

