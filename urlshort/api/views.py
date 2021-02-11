from rest_framework import generics
from ..models import Url
from .serializers import UrlSerializer


class UrlListView(generics.ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

class UrlDetailView(generics.RetrieveAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer