from django.shortcuts import render, redirect
from frige.models import FrigeItem

# Create your views here.
def refrigerator_state(request):
    itemLst = FrigeItem.objects.order_by('drink')

    context = {
        'itemLst' : itemLst
    }
    return render(request, 'frige/state.html', context)

def plus_quantity(request):
    print("Plus")
    return redirect('frige:frige_state')

def minus_quantity(request):
    print("Minus")
    return redirect('frige:frige_state')