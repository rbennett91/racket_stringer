from django.contrib import admin

from .models import Customer, Order, Racket, String

admin.site.register(Racket)
admin.site.register(String)
admin.site.register(Customer)
admin.site.register(Order)
