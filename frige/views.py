from django.shortcuts import render
from frige.models import Frige

# Create your views here.
def refrigerator_state(request):
    drinkLst = Frige.objects.order_by('created_at')

    context = {
        'drinkLst' : drinkLst
    }
    return render(request, 'frige/state.html', context)