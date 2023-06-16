from django.shortcuts import render
from frige.models import Frige, FrigeItem

# 냉장고 state.html
def refrigerator_state(request):
    friges = Frige.objects.all()
    context = {
        'friges': friges
    }
    return render(request, 'frige/state.html', context)
