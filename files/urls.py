from django.urls import path
from files import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('search/', views.SearchView, name="searchview"),
    path('DelRecords/', views.DeleteRecords, name="delrecview"),

]