from django.shortcuts import redirect, render
from django.db.models import Q
from carStore.models import Car
from carStore.forms import CarForm


def cars_view(request):
    search = request.GET.get('search', '')

    cars = Car.objects.all().order_by('model')

    if search:
        terms = search.split()
        
        for term in terms:
            cars = cars.filter(
                Q(model__icontains=term) |
                Q(brand__name__icontains=term)
            ).order_by('model')

    return render(
        request,
        'cars.html',
        {'cars': cars, 'search': search}
    )
    
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(
        request,
        'new_car.html',
        { 'new_car_form': new_car_form }
    )