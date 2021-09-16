from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact


# Create your views here.
def register_view(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password == password2:
			if User.objects.filter(username=username).exists():
					messages.error(request , 'User Name Already Taken')
					return redirect('accounts:register_view')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request , 'Email Name Already Exits ')
					return redirect('accounts:register_view')
				else:
					user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name
						=last_name)
					# auth.login(request , user)
					# messages.success(request,'You Are Now LoggedIn')
					# return redirect('pages:index')
					user.save()
					messages.success(request,'You Are Now Registered')
					return redirect('accounts:login_view')
		else:
			messages.error(request , 'Password Doest Not Match')
			return redirect('accounts:register_view')

	else:
		return render(request,'account/register.html')


def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username , password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request,'You Are Now LoggedIn')
			return redirect('accounts:dashboard')
		else:
			messages.error(request,'Invalid Credentials')
			return redirect('accounts:login_view')
	else:
		return render(request,'account/signin.html')

def logout(request):
	auth.logout(request)
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request,'You Are Now Logged Out')
		return render(request,'core/index.html')
	return redirect('accounts:login_view')

def dashboard(request):
	
	return render(request,'core/dashboard.html')
