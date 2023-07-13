from django.urls import path
from . import views

urlpatterns = [
    path('dogs/', views.DogList.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),
    path('breeds/', views.BreedList.as_view()),
    path('breeds/<str:pk>/', views.BreedDetails.as_view()),
]