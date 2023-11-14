from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/<str:id>', views.getNote, name='note'),
    path('notes/create', views.createNote, name='create'),
    path('notes/<str:id>', views.updateNote, name='update'),
    path('notes/<str:id>', views.deleteNote, name='delete'),
]