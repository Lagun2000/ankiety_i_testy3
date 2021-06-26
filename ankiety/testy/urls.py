from django.urls import path
from .views import Przedmioty_list, Przedmioty_detail

urlpatterns = [
    path('przedmioty', Przedmioty_list),
    path('Przedmioty/<int:pk>', Przedmioty_detail)

]