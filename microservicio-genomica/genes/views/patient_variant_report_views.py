from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import PatientVariantReportService
from ..dtos import PatientVariantReportDTO


class PatientVariantReportListView(APIView):
    """Listar y crear reportes de variantes de pacientes"""

    def __init__(self):
        super().__init__()
        self.report_service = PatientVariantReportService()

    def get(self, request):
        """GET /patient-reports/ - Listar reportes (filtro opcional: ?patient_id=X)"""
        # Ver si viene filtro por paciente
        patient_id = request.query_params.get('patient_id')

        if patient_id:
            reports = self.report_service.get_reports_by_patient(patient_id)
        else:
            reports = self.report_service.get_all_reports()

        reports_dto = [PatientVariantReportDTO(report).to_dict() for report in reports]
        return Response(reports_dto, status=status.HTTP_200_OK)

    def post(self, request):
        """POST /patient-reports/ - Crear un nuevo reporte"""
        report_data = PatientVariantReportDTO.from_request(request.data)
        report = self.report_service.create_report(report_data)
        report_dto = PatientVariantReportDTO(report).to_dict()
        return Response(report_dto, status=status.HTTP_201_CREATED)


class PatientVariantReportDetailView(APIView):
    """Ver, actualizar y eliminar un reporte específico"""

    def __init__(self):
        super().__init__()
        self.report_service = PatientVariantReportService()

    def get(self, request, pk):
        """GET /patient-reports/{id}/ - Obtener un reporte por ID"""
        report = self.report_service.get_report_by_id(pk)
        report_dto = PatientVariantReportDTO(report).to_dict()
        return Response(report_dto, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """PUT /patient-reports/{id}/ - Actualizar un reporte"""
        report_data = PatientVariantReportDTO.from_request(request.data)
        report = self.report_service.update_report(pk, report_data)
        report_dto = PatientVariantReportDTO(report).to_dict()
        return Response(report_dto, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """DELETE /patient-reports/{id}/ - Eliminar un reporte"""
        self.report_service.delete_report(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """PATCH /patient-reports/{id}/ - Actualización parcial"""
        report = self.report_service.get_report_by_id(pk)

        if 'patient_id' in request.data:
            report.patient_id = request.data['patient_id']
        if 'variant_id' in request.data:
            report.variant_id = request.data['variant_id']
        if 'detection_date' in request.data:
            report.detection_date = request.data['detection_date']
        if 'allele_frequency' in request.data:
            report.allele_frequency = request.data['allele_frequency']

        report.save()
        report_dto = PatientVariantReportDTO(report).to_dict()
        return Response(report_dto, status=status.HTTP_200_OK)