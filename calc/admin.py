from django.contrib import admin

# Register your models here.

from .models import Customer, product, order, Tag

admin.site.register(Customer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(Tag)