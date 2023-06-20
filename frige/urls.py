from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'frige'

urlpatterns = [
    path('', refrigerator_state, name = 'frige_state'),
    path("quantity/", handle_quantity, name = 'quantity')
]