from django.shortcuts import render, render_to_response, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, ListForm, ProjectForm
from .models import List, User, Project


# def index(request):
# 	return render(request, 'homeApp/index.html')

def homepage(request):
	return render(request, 'homeApp/home.html')

def calendar(request):
	return render(request, 'homeApp/calendar.html')

def contact(request):
	return render(request, 'homeApp/contact.html')

def dashboard(request):
	L = List.objects.filter(curr_user_id=request.user.id)
	if request.method == 'POST':
		if 'item' in request.POST:
			form = ListForm({'item': request.POST['item']})
			if form.is_valid():
				instance = form.save(commit=False)
				instance.curr_user = request.user
				instance.save()
				# a = list(L.cleaned_data['pk'])
				L = List.objects.filter(curr_user_id=request.user.id).last()
				# print(L.pk)
				data = {'message': "Valid project added method.", 'ID': L.pk}
			else:
				data = {'message': "Invalid project added method.", 'ID': L.pk}
			# return render(request, 'homeApp/demo.html', context={'data': data})
			return JsonResponse(data)
		else:
			ttls = request.POST['value']
			h = ttls[:2]
			m = ttls[3:5]
			s = ttls[-2:]
			t = int(h) + int(m)/60 + int(s)/3600
			form = ProjectForm({'entry_hour': t})
			if form.is_valid():
				instance = form.save(commit=False)
				instance.entry_user = request.user
				# print(request.POST.get('submit'))
				instance.entry_project = List.objects.get(pk=request.POST.get('submit'))
				instance.save()
				data = {
                	'message': "Successfully submitted form data."
            	}
				return JsonResponse(data)
	elif request.method == 'GET' and 'delete' in request.GET:
		# print(request.GET['delete'])
		item = List.objects.get(pk=request.GET['delete'])
		item.delete()
		# messages.success(request, ('Item deleted!'))
	return render(request, 'homeApp/dashboard.html', context={'all_items': L})

def demo(request):
	return render(request, 'homeApp/demo.html')

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Create: {username}")
			login(request, user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	form = NewUserForm
	return render(request, 
					"homeApp/register.html",
					context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "Logged in successfully!")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password!")
		else:
			messages.error(request, "Invalid username or password!")

	form = AuthenticationForm()
	return render(request,
					"homeApp/login.html",
					context={"form":form})