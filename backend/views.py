from django.shortcuts import render
from rest_framework import viewsets
from .models import reportModel
from .serializers import reportSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class report(viewsets.ModelViewSet):
    queryset = reportModel.objects.all()
    serializer_class = reportSerializer


    permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


