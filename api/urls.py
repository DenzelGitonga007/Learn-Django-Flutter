from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes), # get Json Response
    path('notes/', views.getNotes), # get the notes
    path('notes/<str:pk>/', views.getNote), # get the note
]