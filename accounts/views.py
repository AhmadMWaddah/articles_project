from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import FormRegister


def accountLogOut(request):
	logout(request)
	return redirect('view_articles')


def accountRegister(request):
	form_register = FormRegister()

	if request.method == 'POST':
		form_register = FormRegister(request.POST)

		if form_register.is_valid():
			form_register.save()
			return redirect('login')

	else:
		form_register = FormRegister()

	args = {
		'page': 'A.M.W User Sign Up',
		'form_register': form_register,
	}
	return render(request, 'accounts/register.html', args)


def accountLogIn(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		if email and password:
			account = authenticate(email=email, password=password)

			if account is not None:
				login(request, account)
				return redirect('view_articles')
			else:
				messages.error(request, 'Credentials Are Invalid.')

		else:
			messages.error(request, 'Please Provide Email and Password.')
			
	args = {
		'page': 'A.M.W User Sign In',
	}
	return render(request, 'accounts/login.html', args)
