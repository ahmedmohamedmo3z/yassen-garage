from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Car, LicenseImage
from .forms import CarForm


@login_required
def dashboard(request):

    total_cars = Car.objects.count()
    total_images = LicenseImage.objects.count()

    return render(
        request,
        'garage/dashboard.html',
        {
            'total_cars': total_cars,
            'total_images': total_images
        }
    )


@login_required
def cars(request):

    search = request.GET.get('search')

    cars = Car.objects.all()

    if search:
        cars = cars.filter(
            Q(owner_name__icontains=search) |
            Q(phone__icontains=search) |
            Q(plate_number__icontains=search)
        )

    return render(
        request,
        'garage/cars.html',
        {
            'cars': cars
        }
    )


@login_required
def add_car(request):

    if request.method == 'POST':

        form = CarForm(request.POST, request.FILES)

        if form.is_valid():

            car = form.save()

            images = request.FILES.getlist('license_images')

            for image in images:
                LicenseImage.objects.create(
                    car=car,
                    image=image
                )

            return redirect('cars')

    else:
        form = CarForm()

    return render(
        request,
        'garage/add_car.html',
        {
            'form': form
        }
    )


@login_required
def edit_car(request, car_id):

    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':

        form = CarForm(
            request.POST,
            request.FILES,
            instance=car
        )

        if form.is_valid():

            car = form.save()

            images = request.FILES.getlist('license_images')

            for image in images:
                LicenseImage.objects.create(
                    car=car,
                    image=image
                )

            return redirect('cars')

    else:

        form = CarForm(instance=car)

    return render(
        request,
        'garage/add_car.html',
        {
            'form': form
        }
    )


@login_required
def delete_car(request, car_id):

    car = get_object_or_404(Car, id=car_id)

    car.delete()

    return redirect('cars')


@login_required
def car_images(request, car_id):

    car = get_object_or_404(Car, id=car_id)

    images = car.license_images.all()

    return render(
        request,
        'garage/car_images.html',
        {
            'car': car,
            'images': images
        }
    )


@login_required
def delete_image(request, image_id):

    image = get_object_or_404(
        LicenseImage,
        id=image_id
    )

    car_id = image.car.id

    image.delete()

    return redirect(
        'car_images',
        car_id=car_id
    )


@login_required
def toggle_payment(request, car_id):

    car = get_object_or_404(
        Car,
        id=car_id
    )

    car.is_paid = not car.is_paid

    car.save()

    return redirect('cars')


def logout_view(request):

    logout(request)

    return redirect('login')