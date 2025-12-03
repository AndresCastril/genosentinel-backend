class PatientVariantReportDTO:
    """DTO para reportes de pacientes"""

    def __init__(self, report):
        # Datos del reporte más info de la variante
        self.id = report.id
        self.patient_id = report.patient_id
        self.variant_id = report.variant.id
        self.gene_symbol = report.variant.gene.symbol
        self.chromosome = report.variant.chromosome
        self.position = report.variant.position
        # Manejar si es date o string
        if hasattr(report.detection_date, 'isoformat'):
            self.detection_date = report.detection_date.isoformat()
        else:
            self.detection_date = report.detection_date
        self.allele_frequency = float(report.allele_frequency)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'variant_id': self.variant_id,
            'gene_symbol': self.gene_symbol,
            'chromosome': self.chromosome,
            'position': self.position,
            'detection_date': self.detection_date,
            'allele_frequency': self.allele_frequency
        }

    @staticmethod
    def from_request(data):
        return {
            'patient_id': data.get('patient_id'),
            'variant_id': data.get('variant_id'),
            'detection_date': data.get('detection_date'),
            'allele_frequency': data.get('allele_frequency')
        }

    @staticmethod
    def validate_data(data):
        # Validar campos y que allele frequency esté entre 0 y 1
        errors = []

        if not data.get('patient_id'):
            errors.append('patient_id is required')
        if not data.get('variant_id'):
            errors.append('variant_id is required')
        if not data.get('detection_date'):
            errors.append('detection_date is required')

        allele_freq = data.get('allele_frequency')
        if allele_freq is None:
            errors.append('allele_frequency is required')
        elif allele_freq < 0 or allele_freq > 1:
            errors.append('allele_frequency must be between 0 and 1')

        return (len(errors) == 0, errors)