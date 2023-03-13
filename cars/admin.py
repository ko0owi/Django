from django.contrib import admin
from .models import Car, Feature, Category, Department, Order


# Register your models here.
admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(Department)
admin.site.register(Order)
