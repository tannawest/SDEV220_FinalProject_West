from django.urls import path
from . import views

app_name = "foster"

urlpatterns = [
    path("", views.home, name="home"),
    path("foster_families/", views.foster_family_list, name="foster_family_list"),
    path("add_foster_family/", views.add_foster_family, name="add_foster_family"),
    path("pets/", views.pet_list, name="pet_list"),
    path("add_pet/", views.add_pet, name="add_pet"),
    path("edit_pet/<int:pet_id>/", views.edit_pet, name="edit_pet"),
    path("request_foster/<int:pet_id>/", views.request_foster, name="request_foster"),
]
