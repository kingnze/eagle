from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from booking.models import Booking


def register(request):
   if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']
      
      if password == password2:
         if User.objects.filter(username=username).exists():
           messages.error(request, 'Username is taken')
           return redirect('register')
         else:
            if User.objects.filter(email=email).exists():
              messages.error(request, 'Email already in use')
              return redirect('register')
            else:
               # Login after register
               user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
               # auth.login(request, user)
               # messages.success(request, 'Your are logged in')   
               # return redirect('index')
               user.save()
               # messages.success(request, 'You can now log in')
               return redirect('login')
      else:
         messages.error(request, 'Password do not match')
         return redirect('register')
   else: 
      return render(request,'login/register.html')

def login(request):
   if request.method == 'POST':
     username = request.POST['username']
     password = request.POST['password']

     user = auth.authenticate(username=username, password=password)
      
     if user is not None:
        auth.login(request, user)
      #   messages.success(request, 'You are now logged in')
        return redirect('rooms')
     else:
        messages.error(request, 'Invalid credentials')
        return redirect('login')
   else:
      return render(request,'login/login.html')

def logout(request):
   if request.method == 'POST':
     auth.logout(request)
   #   messages.success(request, 'Thanks we hope to see you soon')
     return redirect('index')
     
# def dashboard(request):
#    user_booking = Booking.objects.order_by('-request_date').filter(user_id=request.user.id)
#    context = {
#       'booking': user_booking
#    }
#    return render(request,'login/dashboard.html',context)