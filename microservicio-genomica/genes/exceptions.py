from rest_framework.exceptions import APIException
from rest_framework import status


# Excepciones para cuando no se encuentra algo
class GeneNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Gene not found'
    default_code = 'gene_not_found'


class GeneticVariantNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Genetic variant not found'
    default_code = 'variant_not_found'


class PatientVariantReportNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Patient variant report not found'
    default_code = 'report_not_found'


# Excepciones para validación de datos
class InvalidAlleleFrequencyException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Allele frequency must be between 0 and 1'
    default_code = 'invalid_allele_frequency'


class InvalidGeneDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid gene data provided'
    default_code = 'invalid_gene_data'


class InvalidVariantDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid variant data provided'
    default_code = 'invalid_variant_data'


class InvalidReportDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid report data provided'
    default_code = 'invalid_report_data'