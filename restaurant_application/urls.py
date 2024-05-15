from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Include restaurant app URLs
    path("", include("restaurant.urls")), 
    ] 
