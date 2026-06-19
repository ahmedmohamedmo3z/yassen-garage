from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='garage/login.html'
        ),
        name='login'
    ),

  path(
    'logout/',
    views.logout_view,
    name='logout'
),

    path(
        'add-car/',
        views.add_car,
        name='add_car'
    ),

    path(
        'cars/',
        views.cars,
        name='cars'
    ),

    path(
        'car-images/<int:car_id>/',
        views.car_images,
        name='car_images'
    ),

    path(
        'edit-car/<int:car_id>/',
        views.edit_car,
        name='edit_car'
    ),

    path(
        'delete-car/<int:car_id>/',
        views.delete_car,
        name='delete_car'
    ),

    path(
        'delete-image/<int:image_id>/',
        views.delete_image,
        name='delete_image'
    ),

    path(
        'toggle-payment/<int:car_id>/',
        views.toggle_payment,
        name='toggle_payment'
    ),

]