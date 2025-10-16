from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',view=views.welcome),
    path("details/", view=views.details_view),
    path('details/<int:id>',view=views.single_user),
    path('register/',view=views.register_user)
]
