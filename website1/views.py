from django.shortcuts import render
from website1.forms import LoginForm
import datetime

def home_view(request):
	form=LoginForm()
	return render(request,'website1/home.html',{'form':form})


def date_time_view(request):
	name=request.GET['name']
	response=render(request,'website1/datetime.html',{'name':name})
	response.set_cookie('name',name)
	return response


def result_view(request):
	name=request.COOKIES['name']
	date_time=datetime.datetime.now()
	my_dict={'name':name,'date_time':date_time}
	return render(request,'website1/result.html',my_dict)   
