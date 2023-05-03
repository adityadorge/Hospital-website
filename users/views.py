from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login , logout
from Hospital_App.views import index  
from users.forms import UserRegistrationForm 

def register(request):
	if request.method =='POST':
		form = UserRegistrationForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			print('done')
			user = form.save()
			login(request, user)
			return redirect('Hospital_App:index')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html',  {'form': form})
    
# def register(request):
# 	if request.method=='POST':
# 		form=UserCreationForm(request.POST)
# 		print(form.is_valid())
# 		if form.is_valid():
# 			form.save()
# 			return redirect('Hospital_App:index')
# 	else:
# 		form=UserCreationForm()
# 	return render(request,'users/register.html',{'form':form})

def login_view(request):
	if request.method=='POST':
		form=AuthenticationForm(request,data=request.POST)
		username=request.POST.get('username')
		print(username)
		password = request.POST.get('password') 
		print(password)
		user=authenticate(request,username=username, password=password)
		print(form.is_valid())
		if form.is_valid():
			print("Done")
			login(request,user)
			return redirect('Hospital_App:index')
	else:
		form=AuthenticationForm()
	return render(request, 'users/login.html', {'form':form})
	     

        
def logout_view(request):
	logout(request)
	return render(request, 'users/logout.html')
	