from django.urls import path, include
from .views import *


app_name="countries"

urlpatterns = [
    path('create/', CreateCountryView.as_view()),
    path('list/', CountryListView.as_view()),
    path('detail/<int:pk>/', CountryDetailView.as_view()),
]
