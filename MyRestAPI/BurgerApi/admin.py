from django.contrib import admin
from .models import UserProfile, Ingredient, CustomerDetails, Order

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Ingredient)
admin.site.register(CustomerDetails)
admin.site.register(Order)