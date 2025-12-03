from django.urls import path
from .views import (
    GeneListView,
    GeneDetailView,
    GeneticVariantListView,
    GeneticVariantDetailView,
    PatientVariantReportListView,
    PatientVariantReportDetailView
)

urlpatterns = [
    # Endpoints de genes
    path('genes/', GeneListView.as_view(), name='gene-list'),
    path('genes/<int:pk>/', GeneDetailView.as_view(), name='gene-detail'),

    # Endpoints de variantes genéticas
    path('variants/', GeneticVariantListView.as_view(), name='variant-list'),
    path('variants/<str:pk>/', GeneticVariantDetailView.as_view(), name='variant-detail'),

    # Endpoints de reportes de variantes de pacientes
    path('patient-reports/', PatientVariantReportListView.as_view(), name='report-list'),
    path('patient-reports/<str:pk>/', PatientVariantReportDetailView.as_view(), name='report-detail'),
]