from django.urls import path
from . import views


urlpatterns = [
    path("get_user/",view=views.get_users),
    path("update_user<int:id>/",view=views.update_users),
    path("delete_user<int:id>/",view=views.delete_users),
    path("reg_user/",view=views.reg_users),
]
