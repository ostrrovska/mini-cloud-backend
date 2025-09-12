from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
