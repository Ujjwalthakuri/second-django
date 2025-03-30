from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(order_item)

@admin.register(Category)
class restro(admin.ModelAdmin):
    list_display=("id","name",)
    list_filter = ("name",)
    search_fields=("name",)

class foodadm(admin.ModelAdmin):
    list_display=("id","name",)  
    search_fields=('name',)  
admin.site.register(Food, foodadm)
  
@admin.register(Table)
class tableadm(admin.ModelAdmin):
    list_display=("number",)
    search_fields=("number",)

class orderiteminline(admin.TabularInline):
    model=order_item
    extra=0
    autocomplete_fields=('food_id',)

@admin.register(Order)
class ordersdm(admin.ModelAdmin):
    list_filter=("user","table_id", )
    inlines = [orderiteminline]
