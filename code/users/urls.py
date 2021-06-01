
from django.urls import path, include
from .views import *


app_name="users"

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('list/', UserListView.as_view()),
    path('detail/<int:pk>/', UserDetailView.as_view()),
]
