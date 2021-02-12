from rest_framework import generics
from ..models import Url
from .serializers import UrlSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class UrlListView(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [IsAuthenticated]

class UrlDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [IsAuthenticated]
