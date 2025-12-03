from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Gene, GeneticVariant, PatientVariantReport



class GeneViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestión de genes.
    Proporciona operaciones CRUD completas.
    """
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer


class GeneticVariantViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestión de variantes genéticas.
    Proporciona operaciones CRUD completas.
    """
    queryset = GeneticVariant.objects.all()

    def get_serializer_class(self):
        """
        Usa serializer detallado para retrieve, simple para list.
        """
        if self.action == 'retrieve':
            return GeneticVariantDetailSerializer
        return GeneticVariantSerializer

    @action(detail=False, methods=['get'])
    def by_gene(self, request):
        """
        Endpoint personalizado: GET /variants/by_gene/?gene_id=1
        Filtra variantes por gen.
        """
        gene_id = request.query_params.get('gene_id')
        if not gene_id:
            return Response(
                {'error': 'gene_id parameter is required'},
                status=400
            )

        variants = self.queryset.filter(gene_id=gene_id)
        serializer = self.get_serializer(variants, many=True)
        return Response(serializer.data)


class PatientVariantReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestión de reportes de variantes de pacientes.
    Proporciona operaciones CRUD completas.
    """
    queryset = PatientVariantReport.objects.all()

    def get_serializer_class(self):
        """
        Usa serializer detallado para retrieve, simple para list.
        """
        if self.action == 'retrieve':
            return PatientVariantReportDetailSerializer
        return PatientVariantReportSerializer

    @action(detail=False, methods=['get'])
    def by_patient(self, request):
        """
        Endpoint personalizado: GET /patient-reports/by_patient/?patient_id=xxx
        Filtra reportes por paciente.
        """
        patient_id = request.query_params.get('patient_id')
        if not patient_id:
            return Response(
                {'error': 'patient_id parameter is required'},
                status=400
            )

        reports = self.queryset.filter(patient_id=patient_id)
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)

