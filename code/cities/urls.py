from django.urls import path, include
from .views import *


app_name="cities"

urlpatterns = [
    path('detail/<int:city_pk>/photos/', CityPhotoListView.as_view()),
    path('photos/create/', CreatePhotoView.as_view()),
    path('photos/detail/<int:pk>/', PhotoDetailView.as_view()),
    
    path('create/', CreateCityView.as_view()),
    path('list/', CityListView.as_view()),
    path('detail/<int:pk>/', CityDetailView.as_view()),
]
