from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm,CustomPasswordChangeForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, 'ثبت‌نام شما با موفقیت انجام شد!')
            return redirect('login')  # تغییر به صفحه اصلی
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'خوش آمدید {username}!')
                return redirect('complaint_list')  # تغییر به صفحه اصلی
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید.')
    return redirect('complaint_list')  # تغییر به صفحه اصلی 




@login_required
def custom_password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت!')
            return redirect('complaint_list')  # تغییر به صفحه پروفایل یا صفحه اصلی
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})