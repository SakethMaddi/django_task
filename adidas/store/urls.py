from django.urls import path
from . import views

urlpatterns = [
    path('shoes/',view=views.shoes),
    path('men/',view=views.men),
    path('women/',view=views.women),
    path('kids/',view=views.kids)
]
