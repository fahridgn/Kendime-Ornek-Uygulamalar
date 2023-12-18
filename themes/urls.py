from django.urls import path
from . import views


urlpatterns = [
    path("deney/", views.deneyview, name="deney"),
    path("", views.themeview, name="theme"),
    path("theme/<int:pk>/", views.theme_update, name="theme_update"),
    path("detail/<int:pk>/", views.theme_detail, name="theme_detail"),
    path("delete/<int:pk>/", views.theme_delete, name="theme_delete"),
    path("add/", views.theme_add, name="theme_add"),
]
