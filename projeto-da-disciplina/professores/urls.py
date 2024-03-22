from django.urls import path
from . import views

urlpatterns = [
    path("professores/", views.ProfessorView.as_view()),
    path("professores/<str:pk>/", views.ProfessorDetailView.as_view()),
]
