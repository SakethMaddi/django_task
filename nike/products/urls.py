from django.urls import path
from . import views


urlpatterns = [
    path('cart/',view=views.cart ),
    path('models/',view=views.models),
    path('men/',view=views.men),
    path('women/',view=views.women)
]