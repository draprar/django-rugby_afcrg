from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('archive.urls')),
]

handler404 = 'archive.views.error_404_view'
