from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneViewSet, GeneticVariantViewSet, PatientVariantReportViewSet

router = DefaultRouter()
router.register(r'genes', GeneViewSet, basename='gene')
router.register(r'variants', GeneticVariantViewSet, basename='variant')
router.register(r'patient-reports', PatientVariantReportViewSet, basename='patient-report')

urlpatterns = [
    path('', include(router.urls)),
]
"""

- `DefaultRouter`: Genera automáticamente URLs para todos los endpoints del ViewSet
- `register`: Registra cada ViewSet con su ruta base

"""
