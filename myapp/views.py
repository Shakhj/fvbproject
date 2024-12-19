from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *


# Create your views here.
def display(request):
	s=Student.objects.all()
	d={'stud':s}
	return render(request,'htmlpage/index.html',d)

def insert_view(request):
	f=StudentForm()
	if request.method=="POST":
		f=StudentForm(request.POST)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'form':f}
	return render(request,'htmlpage/insert.html',d)

def delete_view(request,id):
	s=Student.objects.get(id=id)
	s.delete()
	return redirect('/')

def update_view(request,id):
	s=Student.objects.get(id=id)
	if request.method=="POST":
		f=StudentForm(request.POST,instance=s)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'stud':s}
	return render(request,'htmlpage/update.html',d)
    
   
