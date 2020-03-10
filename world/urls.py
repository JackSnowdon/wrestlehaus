from django.urls import path
from .views import *

urlpatterns = [
    path('world_index/', world_index, name="world_index"),
    path('add_wrestler/', add_wrestler, name="add_wrestler"),
    path(r'edit_wrestler/<int:pk>', edit_wrestler, name="edit_wrestler"),
    path(r'delete_wrestler/<int:pk>', delete_wrestler, name="delete_wrestler"),
    path('add_move/', add_move, name="add_move"),
    path(r'edit_move/<int:pk>', edit_move, name="edit_move"),
    path(r'delete_move/<int:pk>', delete_move, name="delete_move"),
]