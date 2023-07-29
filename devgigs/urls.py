from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing>", views.show_listing, name="listing"),
    path("manage", views.manage_view, name="manage")
]