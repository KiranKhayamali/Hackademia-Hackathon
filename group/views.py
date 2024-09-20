from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from group.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from django.template import loader
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy

class Index(View):
    def get(self, request):
        context = {
            "page_name":"Home"
        }
        return render(request,'index.html',context)
      
class Login_view(View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        context = {
            'alert_title': alert_title,
            'alert_detail': alert_detail,
            'page_name': 'login'
        }
        return render(request,"signin.html",context)
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:# checks if the user is logged in or not?
            login(request,user) #logins the user
            return redirect ('/login')
        else:
            request.session['alert_title'] = "Invalid Login Attempt"
            request.session['alert_detail'] = "Please enter valid login credential."
            return redirect(request.path)
        
class Logout_view(View):
    def get(self,request):
        request.session.clear()
        logout(request)
        return redirect('/')


class Signup_View (View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        context = {
            'alert_title':alert_title,
            'alert_detail':alert_detail,
            'page_name': 'Signup'
        }
        return render(request,"signup.html",context)
        
    def post(self,request):
        if request.method == 'POST':
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            username = request.POST.get('username')
            email = request.POST.get('email') #validation required
            password = request.POST.get('password')
            status = request.POST.get('status')

            #determine type of user
            if status == 'admin':
                is_superuser = True 
                is_staff = True
            elif status == 'seller':
                is_superuser == False
                is_staff = True
            elif status =='customer':
                is_staff = False
                is_superuser = False

                
            user = User.objects.create_user(username , email, password,is_superuser=is_superuser,is_staff = is_staff)
            user.save()

            #additional user details
            user.first_name=firstName
            user.last_name=lastName
            user.save()
            user = authenticate(username = username, password = password)
            if user is not None:# checks if the user is logged in or not?
                login(request,user) #logins the user
            return redirect ('/')  


class teacher_form_view(View):
    def get(self, request):
        context = {
            "page_name":"teacher signup"
        }
        return render(request,'teacher.html',context)  

# login and sign up related views
