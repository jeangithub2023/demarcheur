from django.contrib import admin
from menage.models import Menus, Services, Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=['user','service','phone','adresse','ordered_date']
admin.site.register(Menus)
admin.site.register(Services)
admin.site.register(Order, OrderAdmin)