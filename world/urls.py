from django.urls import path
from .views import *

urlpatterns = [
    path('world_index/', world_index, name="world_index"),
    path('add_wrestler/', add_wrestler, name="add_wrestler"),
    path(r'edit_wrestler/<int:pk>', edit_wrestler, name="edit_wrestler"),
    path(r'delete_wrestler/<int:pk>', delete_wrestler, name="delete_wrestler"),
]