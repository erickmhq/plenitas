from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from .serializers import DeviceSerializer, UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class DeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.devices.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)