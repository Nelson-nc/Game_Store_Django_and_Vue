from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
        model = Customer
        fields = ["id", "user", "address", "phone_no"]
        readonly_fields = ["id"]
        list_display = ["id", "user", "address", "phone_no"]


admin.site.register(Customer, CustomerAdmin)