from django.urls import path
from . import views


urlpatterns = [
    path("get_users/",view=views.get_users),
    path("reg_user/",view=views.reg_user),
    # path("update_users/",view=views.update_users),
    # path("delete_users/",view=views.delete_users),
]
