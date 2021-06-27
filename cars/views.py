from django.shortcuts import render, get_object_or_404
from .models import Car
# Create your views here.

def cars(request):
    cars=Car.objects.order_by("-created_date")

    data={"cars":cars,}
    return render(request,'cars/cars.html',data)


#get_object_or_404 function is used to fetch single car object from database else it will return error 404 if no object on the basis of priary key=id
def car_detail(request, id):

    single_car= get_object_or_404(Car,pk=id)

    data={'single_car':single_car,}
    return render(request,'cars/car_detail.html',data)