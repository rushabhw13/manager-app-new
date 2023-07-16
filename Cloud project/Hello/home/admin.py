from django.contrib import admin
from home.models import Restaurant, Menu, Staff, Tables, Todayspecial
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Staff)
admin.site.register(Tables)
admin.site.register(Todayspecial)