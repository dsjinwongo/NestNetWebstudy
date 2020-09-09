from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('schedule/<int:sche_id>/', views.detail, name = 'detail'),
    path('schedule/new/', views.sche_new, name = 'new'),
    path('schedule/<int:sche_id>/edit/', views.sche_edit, name = 'edit'),
    path('schedule/<int:sche_id>/delete/', views.sche_delete, name = 'delete'),
]