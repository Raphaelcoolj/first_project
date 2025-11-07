from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from .models import Wallet
from .serializers import WalletSerializer, UserSerializer



from django.http import HttpResponse
from django.core.management import call_command

def collect_static_view(request):
    call_command("collectstatic", "--noinput")
    return HttpResponse("Static collected")




class IsAdminOrOwnerReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.user == request.user or request.user.is_staff
        return request.user.is_staff

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff


class WalletViewSet(viewsets.ModelViewSet):
   
    serializer_class = WalletSerializer
    permission_classes = [IsAdminOrOwnerReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Wallet.objects.all()
        return Wallet.objects.filter(user=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
       print("Request data:", request.data)
       return super().create(request, *args, **kwargs)
