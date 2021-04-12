from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm, PasswordChangeForm, SetPasswordForm
from enroll.forms import UserSignUp,EditUserForm, EditAdminForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

#Home Page
def addAndShow(request):
    if request.user.is_superuser:
        if request.method=='POST':
            fm=UserSignUp(request.POST)
            if fm.is_valid():
                print(fm.cleaned_data['password1'])
                fm.save()
                messages.success(request,'User Added')
                HttpResponseRedirect('/sprusr/') 
        else:
            fm=UserSignUp()  
        st=User.objects.all()

        return render(request,'adminpanel/addshow.html',{'form':fm,'stud':st})
    else:
        messages.warning(request,"You can't access the admin panel because, You are not an Admin.")
        return HttpResponseRedirect('/profile/')
#Delete Data
def deleteData(request,my_id):
    if request.method=='POST':
        pi=User.objects.get(pk=my_id)
        pi.delete()
        if User.objects.all():
            messages.warning(request,'User Deleted!!!')

        return HttpResponseRedirect('/sprusr/')
def updateData(request,my_id):
    if request.method=='POST':
        pi=User.objects.get(pk=my_id)
        if request.user.is_superuser == True:
            fm=EditAdminForm(data=request.POST,instance=pi)
        else:
            fm=EditUserForm(data=request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.warning(request,'User Deleted!!!')
            return HttpResponseRedirect('/sprusr/')# have to redirect admin panel with message
    else:
        pi=User.objects.get(pk=my_id)
        if request.user.is_superuser == True:
            fm=EditAdminForm(instance=pi)
        else:
            fm=EditUserForm(instance=pi)
    return render(request,'adminpanel/update.html',{'form':fm,'my_id':my_id}) #my_id is pass to update.html template where it will use in url






    

