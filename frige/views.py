from django.shortcuts import render
from frige.models import FrigeItem

# Create your views here.
def refrigerator_state(request):
    itemLst = FrigeItem.objects.order_by('drink')

    context = {
        'itemLst' : itemLst
    }
    return render(request, 'frige/state.html', context)