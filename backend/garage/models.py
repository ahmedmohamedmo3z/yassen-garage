from django.db import models


class Car(models.Model):
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    car_type = models.CharField(max_length=100)
    car_color = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=30, unique=True)

    # حالة الدفع
    is_paid = models.BooleanField(default=False)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.owner_name


class LicenseImage(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='license_images'
    )

    image = models.ImageField(upload_to='licenses/')

    def __str__(self):
        return f"License Image - {self.car.owner_name}"