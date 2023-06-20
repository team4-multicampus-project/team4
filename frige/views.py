from django.shortcuts import render, redirect
from frige.models import Frige, FrigeItem
from django.views.decorators.csrf import csrf_exempt
import json

# 냉장고 state.html
def refrigerator_state(request):
    friges = Frige.objects.all()
    context = {
        'friges': friges
    }
    return render(request, 'frige/state.html', context)

@csrf_exempt
def handle_quantity(request):
    if request.method == "POST":
        data = json.loads(request.body)
        frigeItems = FrigeItem.objects.all()
        
        frige_id, drink, quan = data.split("/")
        print(frige_id, drink, quan)
        frige_id = frige_id[-1]
        drink = drink[1:]
        
        for item in frigeItems:
            if item.frige.id == int(frige_id) and item.drink.name == drink:
                item.quantity = quan
                item.save()
                print(f"Drink : {item.drink.name}, Quan : {item.quantity}")
        
        return redirect("frige:frige_state")