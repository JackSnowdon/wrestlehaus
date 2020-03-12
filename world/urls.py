from django.urls import path
from .views import *

urlpatterns = [
    path('world_index/', world_index, name="world_index"),
    path('add_wrestler/', add_wrestler, name="add_wrestler"),
    path(r'edit_wrestler/<int:pk>', edit_wrestler, name="edit_wrestler"),
    path(r'delete_wrestler/<int:pk>', delete_wrestler, name="delete_wrestler"),
    path(r'single_wrestler/<int:pk>', single_wrestler, name="single_wrestler"),
    path('add_move/', add_move, name="add_move"),
    path(r'edit_move/<int:pk>', edit_move, name="edit_move"),
    path(r'delete_move/<int:pk>', delete_move, name="delete_move"),
    path(r'single_move/<int:pk>', single_move, name="single_move"),
    path('promotions/', promotions, name="promotions"),
    path('add_promotion/', add_promotion, name="add_promotion"),
    path(r'edit_promotion/<int:pk>', edit_promotion, name="edit_promotion"),
    path(r'delete_promotion/<int:pk>', delete_promotion, name="delete_promotion"),
    path(r'single_promotion/<int:pk>', single_promotion, name="single_promotion"),
    path('add_match/', add_match, name="add_match"),
    path(r'delete_match/<int:pk>', delete_match, name="delete_match"),
]