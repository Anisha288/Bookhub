from django.shortcuts import render,redirect
from django.contrib import messages
from app_authenticate.forms import SignUpForm,UserProfileChange,ProfilePic
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail
def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        x = request.POST['email']
        if User.objects.filter(email=x).exists():
            messages.warning(request,'Email already exists')
            return redirect('signup')
        else:

            if form.is_valid():
                    username = form.cleaned_data.get("username")
                    email_register = form.cleaned_data.get("email")

            # Email Sending Body
                    subject = 'User got Register Successfully'
                    message = f'Hello {username}, \n Welcome to the kingdom of books'
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [email_register]
                    fail_silently = True      # To raise any Email exception, we can write False also

                    send_mail(subject,message,from_email,to_list,fail_silently)

                    form.save()
                    registered = True

    context = {'form':form, 'registered':registered }
    return render(request, 'app_authenticate/signup.html',context)

def login_page(request):
        form = AuthenticationForm()
        if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
        if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                        login(request,user)
                        return render(request, 'base.html')
        return render(request,'app_authenticate/login.html',context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('base')    

# Profile landing page
@login_required
def profile(request):
    return render(request,'app_authenticate/profile.html', context={})


# Complete or Change Profile Details
@login_required
def change_profile(request):
    current_user = request.user 
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return render(request,'app_authenticate/profile.html', context={'form':form})
    return render(request, 'app_authenticate/change_profile.html', context={'form':form}) 


@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            print(user_obj)
            user_obj.user = request.user
            user_obj.save()
            
            return render(request,'app_authenticate/profile.html', context={})
    return render(request,'app_authenticate/pro_pic_add.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return render(request,'app_authenticate/profile.html', context={})
    return render(request,'app_authenticate/pro_pic_add.html', context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
            logout(request)      # With change of password user need to Login again
            return redirect('base')
    return render(request,'app_authenticate/pass_change.html', context={'form':form,'changed':changed})    
