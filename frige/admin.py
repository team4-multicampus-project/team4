from django.contrib import admin
from .models import Frige, Drink, FrigeItem
    
class DrinkAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['user','id', 'name','ml']
    ordering = ['id']
    
class FrigeAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['user','id', 'name', 'get_drinks', 'created_at']
    ordering = ['id']
    
    def get_drinks(self, obj):
        return ", ".join([str(item.drink) for item in obj.items.all()])
    get_drinks.short_description = 'Drinks'

    
class FrigeItemAdmin(admin.ModelAdmin):
    search_fields = ['frige']
    list_display = ['user','frige', 'drink', 'quantity']
    ordering = ['frige']
    
admin.site.register(Frige, FrigeAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(FrigeItem, FrigeItemAdmin)

# Register your models here.
