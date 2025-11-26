from ..models import PatientVariantReport
from ..exceptions import (
    PatientVariantReportNotFoundException,
    InvalidReportDataException,
    InvalidAlleleFrequencyException
)
from ..dtos import PatientVariantReportDTO
from .interfaces.ipatient_variant_report_service import IPatientVariantReportService
from .genetic_variant_service import GeneticVariantService


class PatientVariantReportService(IPatientVariantReportService):
    """Servicio para manejar reportes de variantes de pacientes"""

    def __init__(self):
        self.variant_service = GeneticVariantService()

    def get_all_reports(self):
        return PatientVariantReport.objects.all()

    def get_report_by_id(self, report_id):
        try:
            return PatientVariantReport.objects.get(id=report_id)
        except PatientVariantReport.DoesNotExist:
            raise PatientVariantReportNotFoundException()

    def get_reports_by_patient(self, patient_id):
        # Filtrar reportes por paciente
        return PatientVariantReport.objects.filter(patient_id=patient_id)

    def create_report(self, report_data):
        # Validar datos
        is_valid, errors = PatientVariantReportDTO.validate_data(report_data)
        if not is_valid:
            raise InvalidReportDataException(detail=errors)

        # Verificar que la variante exista
        variant_id = report_data.get('variant_id')
        self.variant_service.get_variant_by_id(variant_id)

        # Validación extra de allele frequency (por si acaso)
        allele_freq = report_data.get('allele_frequency')
        if allele_freq < 0 or allele_freq > 1:
            raise InvalidAlleleFrequencyException()

        # Crear reporte
        report = PatientVariantReport(**report_data)
        report.save()
        return report

    def update_report(self, report_id, report_data):
        # Buscar reporte
        report = self.get_report_by_id(report_id)

        # Validar datos
        is_valid, errors = PatientVariantReportDTO.validate_data(report_data)
        if not is_valid:
            raise InvalidReportDataException(detail=errors)

        # Si se cambia la variante, verificar que exista
        if 'variant_id' in report_data:
            self.variant_service.get_variant_by_id(report_data['variant_id'])

        # Validar allele frequency si viene en los datos
        if 'allele_frequency' in report_data:
            allele_freq = report_data['allele_frequency']
            if allele_freq < 0 or allele_freq > 1:
                raise InvalidAlleleFrequencyException()

        # Actualizar campos
        report.patient_id = report_data.get('patient_id', report.patient_id)
        report.variant_id = report_data.get('variant_id', report.variant_id)
        report.detection_date = report_data.get('detection_date', report.detection_date)
        report.allele_frequency = report_data.get('allele_frequency', report.allele_frequency)
        report.save()

        return report

    def delete_report(self, report_id):
        report = self.get_report_by_id(report_id)
        report.delete()