from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include('career.urls')),
    path('', include('course.urls')),
    path('', include('chat.urls')),
]
