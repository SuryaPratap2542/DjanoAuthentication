from django.shortcuts import render ,HttpResponseRedirect
from .forms import SignUpForm,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def Sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account Created successfully")
            fm.save()
    else:
        fm=SignUpForm()
    return render(request, 'enroll/signup.html',{'form':fm})


# login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                usname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=usname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Login successfully !!")
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

#profile 
def user_profile(request):        
    if request.user.is_authenticated: # This is used for check user is authenticated or not if yes then enter otherwise redirect into login page
        if request.method=="POST":
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,"Updated successfully !!")
                fm.save()
        else:
            fm=EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')


#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#Change Password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password Change successfully")
                return HttpResponseRedirect('/profile/')

        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html/',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
#Change Password with old password
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password Change successfully")
                return HttpResponseRedirect('/profile/')

        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'enroll/changepass1.html/',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
