from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import ExlFileSerializer, ExlFileStatusSerializer
from .models import ExlFile


class UploadFile(generics.CreateAPIView):
    serializer_class = ExlFileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, title=self.request.data["xlfile"].name)


class GetStatus(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    queryset = ExlFile.objects.all()
    serializer_class = ExlFileStatusSerializer
