from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request,'accounts/login.html')

def register(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if(not User.objects.filter(username=username).exists()):
                if(not User.objects.filter(email=email).exists()):
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)

                    # To automatically login the created user, include this code also.
                    # auth.login(request, user)
                    # messages.success(request, 'You are logged in.')
                    # return redirect('dashboard')


                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
                else:
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
            else:
                messages.error(request, 'Username already exists!')
                return redirect('register')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('register')




    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):

    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries':user_inquiry,
    }
    return render(request, 'accounts/dashboard.html',data)



