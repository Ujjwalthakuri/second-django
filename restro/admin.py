from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(order_item)

@admin.register(Category)
class restro(admin.ModelAdmin):
    list_display=("name",)
    list_filter = ("name",)
    search_fields=("name",)

class foodadm(admin.ModelAdmin):
    list_display=("name",)    
admin.site.register(Food, foodadm)
  
@admin.register(Table)
class tableadm(admin.ModelAdmin):
    list_display=("number",)
    search_fields=("number",)
    
@admin.register(Order)
class ordersdm(admin.ModelAdmin):
    list_filter=("user","table_id", )
