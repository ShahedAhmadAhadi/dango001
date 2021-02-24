from . import views
from django.urls import path

urlpatterns = [
    path('food/', views.index),
    path('<int:item_id>/', views.detail, name="detail"),
    path('add', views.create_item, name="create_item"),
]