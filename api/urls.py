from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletViewSet, create_admin_view

router = DefaultRouter()
router.register('wallets', WalletViewSet, basename='wallet')

urlpatterns = [
    path('', include(router.urls)),
    path("create/", create_admin_view)
]
