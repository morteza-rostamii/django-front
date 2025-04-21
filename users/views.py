from django.shortcuts import render
# form validation
from .forms import LoginForm
# time
# from datetime import datetime
from datetime import timedelta
from django.utils import timezone
# notification
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# def login_view(request):
#   if request.method == 'POST':
#     form = AuthenticationForm(data=request.POST)
#     if form.is_valid():
#       user = form.get_user()
#       login(request, user)
#       return redirect('index')
#   else:
#     form = AuthenticationForm()
#   return render(request, 'users/login.html', {'form': form})

def login_view(request):

  # on form submit
  if request.method == 'POST':
    print("*****************55", request.POST)
    form = LoginForm(request.POST)
    
    if form.is_valid():
      # redirect to: rise_group:index
      return redirect('rise_group:index-view')

    else:
      request.session['form_errors'] = form.errors
      request.session['form_data'] = request.POST.dict()
      return redirect('users:login-view')  # redirect to GET


  # on GET : reset errors
  else:
    # Rebuild form from session if there were errors
    errors = request.session.pop('form_errors', None)
    data = request.session.pop('form_data', None)
    if errors and data:
      form = LoginForm(data)
      form._errors = errors  # manually assign errors
    else:
      form = LoginForm()
  
  print("*****************")
  print(form.errors)
  return render(request, 'users/login.html', {'form': form})

def logout(request):
  logout(request)
  return redirect('login')

# forget password view
def forgot_password_view(request):

  if request.method == 'POST':
    # redirect to reset-password
    return redirect('users:reset-password-view')

  return render(request, 'users/forgot-password.html')

# reset password view
def reset_password_view(request):

  # generate a date and add 20 seconds to it
  # otp_expiry_time = datetime.now() + timedelta(seconds=20)

  otp_expiry_time = timezone.now() + timedelta(seconds=120)

  if request.method == 'POST':
    # set a message
    messages.success(request, "رمز عبور شما با موفقیت تغییر کرد")
    # messages.error(request, "رمز عبور شما با موفقیت تغییر نکرد")
    #messages.info(request, "رمز عبور شما با موفقیت تغییر کرد")

    print('**88')
    return redirect("users:reset-password-view")

  return render(request, 'users/reset-password.html', {'otp_expiry_time': otp_expiry_time.isoformat()})

# def signup_view(request):
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('home')
#   else:
#       form = UserCreationForm()
#   return render(request, 'authapp/signup.html', {'form': form})

# @login_required
# def profile_view(request):
#   return render(request, 'authapp/profile.html')
