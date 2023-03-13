from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=24, default='standard', unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Feature(models.Model):
    feature = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.feature


class Department(models.Model):

    country = models.CharField(max_length= 32, blank=True)
    city = models.CharField(max_length= 64)
    street_address = models.CharField(max_length= 64)
    post_code = models.CharField(max_length= 10)
    description = models.TextField(max_length=512, blank=True)
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Manager',
        limit_choices_to={'groups__name': 'managers'},
        related_name='managers_set'
    )

    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', ('manual gear')),
        ('automatic', ('automatic gear')),
    ]
    ENGINE_CHOICES = [
        ('diesel', ('diesel')),
        ('petrol', ('petrol')),
        ('electric', ('electric')),
    ]

    brand = models.CharField(max_length= 32)
    model = models.CharField(max_length= 32)
    image = models.ImageField(upload_to='cars/', blank=True)
    description = models.TextField(max_length=512, blank=True)
    engine_type = models.CharField(max_length= 32, choices=ENGINE_CHOICES, default='diesel')
    engine_capacity = models.PositiveSmallIntegerField(help_text="engine capacity in cm³")
    engine_power = models.PositiveSmallIntegerField(help_text="engine power in HP")
    transmission_type = models.CharField(max_length= 32, choices=TRANSMISSION_CHOICES, default='manual')
    seats_no = models.PositiveSmallIntegerField(help_text="number of seats")
    luggage_compartment = models.PositiveSmallIntegerField(help_text="number of bags")
    is_available = models.BooleanField(default=True)

    features = models.ManyToManyField(Feature)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # departments = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"[{self.category}] {self.brand} {self.model}, {self.transmission_type}, {self.engine_power}HP {self.engine_type}"


class Order(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length= 32, blank=True)
    start_rent = models.CharField(max_length= 32, blank=True)
    stop_rent = models.CharField(max_length= 32, blank=True)
