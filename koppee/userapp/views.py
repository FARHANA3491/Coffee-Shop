from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username Already exist")
                return render(request,'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email Already exist")
                return render(request,'signup.html')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,"Account created Successfully, Please Login again")
                # return redirect('/')
        else:
            messages.error(request,"Password do not match")
            return render(request,'signup.html')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            # messages.success(request,"logged in successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid User, Register if you are not")
            return render(request,'signup.html')
    else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')