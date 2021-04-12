from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .forms import UserSignUp,EditUserForm, EditAdminForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

#signup
def signUp(request):
    if request.method == 'POST':
       fm=UserSignUp(request.POST) 
       if fm.is_valid():
           fm.save()
           return HttpResponseRedirect('/login/')
    else:
        fm=UserSignUp()
    fm.order_fields(field_order=['username','email',])
    return render(request,'enroll/signuppage.html',{'form':fm})


#Login
def LogIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Successfuly Loggedin")
                    return HttpResponseRedirect('/profile/')
                
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/loginpage.html',{'form':fm})
    else:
        messages.warning(request,"Already Loggedin")
        return HttpResponseRedirect('/profile/')

#profile
def profile(request):
    if request.user.is_authenticated: #If user is not logged in and directly trying to access profile page then it will redirect to login page.
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm=EditAdminForm(instance=request.user, data = request.POST)
            else:
                fm=EditUserForm(instance=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile Updated')
                return HttpResponseRedirect('/profile/')
                
        else:
            if request.user.is_superuser == True:
                fm=EditAdminForm(instance=request.user)
            else:
                fm=EditUserForm(instance=request.user)
        return render(request,'enroll/profilepage.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#logout
def logOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')
#Update Userpassword with old password
def updatePassword1(request):
    if request.user.is_authenticated:
        if request.method ==  'POST':
            fm=PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)


        return render(request,'enroll/updatepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#Update Userpassword without old password
def updatePassword2(request,my_id):
    if request.user.is_authenticated:
        if request.method ==  'POST':
            pi=User.objects.get(pk=my_id)
            fm=SetPasswordForm(user=pi, data=request.POST)
            if fm.is_valid():
                fm.save()
                #update_session_auth_hash(request,fm.user)
                messages.success(request,'%s\'s password updated'%pi.username)
                return HttpResponseRedirect('/sprusr/')
        else:
            fm=SetPasswordForm(user=request.user)


        return render(request,'enroll/updatepassword1.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
def forgotpass(request):
    if not request.user.is_superuser:
        messages.warning(request,'Please contact admin to reset your password on admin@auth.com')
    else:
        messages.success(request,'please go through with update option on admin panel')
    return HttpResponseRedirect('/profile/')
