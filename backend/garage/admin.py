from django.contrib import admin
from .models import Car, LicenseImage


class LicenseImageInline(admin.TabularInline):
    model = LicenseImage
    extra = 1


class CarAdmin(admin.ModelAdmin):
    inlines = [LicenseImageInline]


admin.site.register(Car, CarAdmin)