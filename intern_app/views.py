from django.shortcuts import render,redirect,HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from django.contrib import auth


def index(request):
	return render(request,'intern_app/home.html')

def home(request):
	if request.user.is_authenticated:
		mail = request.user.email
		c = connection.cursor()
		c.execute("select * from auth_user")
		res= c.fetchall()
		results={
			'users': res
		}
		print(results)
		if(mail == 'pothalavamsi@gmail.com'):
			return render(request, 'intern_app/admin.html', results)
		else:
			return render(request, 'intern_app/user.html')

def user_logout(request):
	auth.logout(request)
	return redirect(index)