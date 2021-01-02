from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

from store.utils import cartData
from store.models import *
from django.http import JsonResponse
import json

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm



def register(request):

	data = cartData(request)
	cartItems = data['cartItems']

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Congrats! Your account is created. You can now log in.')
			return redirect('login') 
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form, 'cartItems': cartItems})




def logout_request(request):
	logout(request)

	data = cartData(request)
	cartItems = data['cartItems']
	return render(request, 'users/logout.html', {'cartItems': cartItems})




def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()

	data = cartData(request)
	cartItems = data['cartItems']
	return render(request = request,
    				template_name = "users/login.html",
    				context={'form':form, 'cartItems': cartItems})




@login_required
def profile(request):
	data = cartData(request)
	cartItems = data['cartItems']


	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
		messages.success(request, f'Your profile is updaited!')
		return redirect('profile') 

	else:
		u_form = UserUpdateForm(instance=request.user)

	context = {
		'cartItems': cartItems,
		'u_form': u_form
		}

	return render(request, 'users/profile.html', context)




