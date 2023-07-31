from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("show/<int:listing>", views.show_listing, name="show"),
    path("manage", views.manage_view, name="manage"),
    path("create", views.create_listing, name="create"),
    path("edit/<int:listing_id>", views.edit_listing, name="edit"),
    path("delete/<int:listing_id>", views.delete_listing, name="delete"),

    # API endpoints
    path("listing/<int:listing>", views.get_listing, name="listing")
]