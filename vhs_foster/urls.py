from django.contrib import admin
from django.urls import path
from foster import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('pets/', views.pet_list, name='pet_list'),
    path('request-foster/<int:pet_id>/', views.request_foster, name='request_foster'),
    path('edit-pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('add-pet/', views.add_pet, name='add_pet'),
    path('add-foster-family/', views.add_foster_family, name='add_foster_family'),
    path('foster-families/', views.foster_family_list, name='foster_family_list'),
]
