from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'frige'

urlpatterns = [
    path('', refrigerator_state, name = 'frige_state'),
    path('plus/', plus_quantity, name="plus_quantity"),
    path('minus/', minus_quantity, name="minus_quantity"),
]