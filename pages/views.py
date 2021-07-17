from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from .models import Contactus
from django.contrib import messages
# Create your views here.

def home(request):
    teams= Team.objects.all()

    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)

    all_cars = Car.objects.order_by('-created_date')

    #search_fields = Car.objects.values('model', 'city', 'year', 'body_style')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()


    data = {'teams':teams,
            'featured_cars':featured_cars,
            'all_cars':all_cars,
            'model_search':model_search,
            'city_search':city_search,
            'year_search':year_search,
            'body_style_search':body_style_search,}

    return render(request,'pages/index.html',data)

def about(request):
    teams = Team.objects.all()

    data = {'teams': teams}
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        contactus = Contactus(name=name, email=email, subject=subject, phone=phone, message=message)

        contactus.save()
        return redirect('home')
    return render(request,'pages/contact.html')


