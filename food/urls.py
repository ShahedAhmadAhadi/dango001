from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:item_id>/', views.detail, name="detail"),
]