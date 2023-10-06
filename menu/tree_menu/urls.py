from django.contrib import admin
from django.urls import path
from menu.tree_menu import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<str:url>/", views.tree_view, name="tree"),
]