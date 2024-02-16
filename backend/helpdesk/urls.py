from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from helpdesk.core.api.viewsets import SectorViewSet, TicketViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'sectors', SectorViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]