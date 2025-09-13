from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.permissions import IsAuthenticated

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Цей view має повертати список документів
        тільки для поточного аутентифікованого користувача.
        """
        return Document.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        При збереженні нового документа, автоматично
        прив'язуємо його до поточного користувача.
        """
        serializer.save(user=self.request.user)