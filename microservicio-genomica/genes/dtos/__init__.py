# Importar todos los DTOs
from .gene_dto import GeneDTO
from .genetic_variant_dto import GeneticVariantDTO
from .patient_variant_report_dto import PatientVariantReportDTO

__all__ = [
    'GeneDTO',
    'GeneticVariantDTO',
    'PatientVariantReportDTO'
]