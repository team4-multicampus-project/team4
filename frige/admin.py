from django.contrib import admin
from .models import Frige, Drink, FrigeItem
    
class DrinkAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id', 'name', 'ml']
    ordering = ['id']
    
class FrigeAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id', 'name', 'user', 'drink', 'created_at']
    ordering = ['id']
    
class FrigeItemAdmin(admin.ModelAdmin):
    search_fields = ['frige']
    list_display = ['frige', 'drink', 'quantity', 'user']
    ordering = ['frige']
    
admin.site.register(Frige, FrigeAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(FrigeItem, FrigeItemAdmin)

# Register your models here.
