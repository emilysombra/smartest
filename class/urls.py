from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClassViewSet


router = DefaultRouter()
router.register(r'class', ClassViewSet, basename='classes')

urlpatterns = [
    path('', include(router.urls))
]
