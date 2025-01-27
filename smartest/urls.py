from django.contrib import admin
from django.urls import path, include
from .docs import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('custom_auth.urls')),
    path('', include('career.urls')),
    path('', include('course.urls')),
    path('', include('chat.urls')),
] + swagger_urls
