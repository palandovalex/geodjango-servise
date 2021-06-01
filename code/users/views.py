from rest_framework import generics, permissions
from .serializers import UserDetailSerializer, UserListSerializer
from .models import User


class CreateUserView(generics.CreateAPIView):
    permission_class = [permissions.IsAdminUser]
    serializer_class = UserDetailSerializer

    
class UserListView(generics.ListAPIView):
    permission_class = [permissions.IsAdminUser]
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [permissions.IsAdminUser]
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
