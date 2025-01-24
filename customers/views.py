from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer
# Create your views here.
def sign_out(request):
     logout(request)
     return redirect('index')
def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
       

                username=request.POST.get('username')
                password=request.POST.get('password')
                email=request.POST.get('email')
                address=request.POST.get('address')
                phone=request.POST.get('phone')

                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    
                )
                customer=Customer.objects.create(
                    name=username, 
                    user=user,
                    address=address,
                    phone=phone,
                )
                success_message='User Registered Successfull'
                messages.success(request,success_message)
                #return redirect('index')
        except Exception as e:
             error_message='Dupilicate user or Invalid Inputs'
             messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
         context['register']=False
         username=request.POST.get('username')
         password=request.POST.get('password')
         print(username,password)
         user=authenticate(username=username,password=password)
         print(user)
         if user:
              login(request,user)
              return redirect('index')
         else:
             error_message='invalid user credentials'
             messages.error(request,error_message)
              
          
                 
    return render(request,'account.html',context)