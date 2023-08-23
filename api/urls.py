from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes), # get Json Response
    path('notes/', views.getNotes), # get the notes
    path('notes/create/', views.createNote), # create note
    path('notes/<str:pk>/', views.getNote), # get the note
    path('notes/<str:pk>/update', views.updateNote), # update the note
    path('notes/<str:pk>/delete', views.deleteNote), # delete the note
    
    
]