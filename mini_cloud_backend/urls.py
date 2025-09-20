from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from documents.views import DocumentViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('authentication.urls')),
    path('', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)