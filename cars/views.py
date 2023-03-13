from django.shortcuts import render, get_object_or_404,redirect
from . models import Car, Order
from .forms import OrderForm


# list of the whole fleet
def fleet(request):
    cars = Car.objects.all()

    context = {
        'page_title': "Our fleet",
        'cars': cars,
    }

    return render(
        request,
        'cars/cars.html',
        context=context
    )


def details(request, car_id):
    """details of selected car"""
    car = get_object_or_404(Car, id=car_id)


    if request.method == "POST":
        if request.user.is_authenticated:

            data = request.POST
            Order.objects.create(
                phone=data.get('phone'),
                start_rent=data.get('start'),
                stop_rent=data.get('stop'),
                name=request.user,
                car=car,
            )

        return redirect ('cars:fleet')

    context = {
        'page_title': "Our fleet",
        'car': car,
    }
    return render(
        request,
        'cars/details.html',
        context=context
    )



def form(request):


    form = OrderForm(request.POST)



    return render (
        request,
        'cars/form.html',
        context={'form' : form}
    )

