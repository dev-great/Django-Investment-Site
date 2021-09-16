from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Contact

# Create your views here.
def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']

		contact = Contact(name=name,email=email,phone=phone, message=message,user_id = user_id)
		contact.save()
		
		messages.success(request,'Your Request has Been Submitted')
		return render(request , 'contact/contact.html')

	else:
		return render(request,'contact/contact.html')


