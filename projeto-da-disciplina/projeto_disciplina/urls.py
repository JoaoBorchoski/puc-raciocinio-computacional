from drf_spectacular.views import SpectacularAPIView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/", include("users.urls")),
    path("api/", include("professores.urls")),
]
