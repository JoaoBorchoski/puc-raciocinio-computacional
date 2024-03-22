from .serializers import ProfessorSerializer
from .models import Professor
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
)
from rest_framework import generics


class ProfessorView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAdminUser()]


class ProfessorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_url_kwarg = "pk"
