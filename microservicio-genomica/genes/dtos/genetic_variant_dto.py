class GeneticVariantDTO:
    """DTO para variantes genéticas"""

    def __init__(self, variant):
        # Guardamos los datos de la variante y su gen relacionado
        self.id = variant.id
        self.gene_id = variant.gene.id
        self.gene_symbol = variant.gene.symbol
        self.gene_name = variant.gene.full_name
        self.chromosome = variant.chromosome
        self.position = variant.position
        self.reference_base = variant.reference_base
        self.alternate_base = variant.alternate_base
        self.impact = variant.impact

    def to_dict(self):
        return {
            'id': self.id,
            'gene_id': self.gene_id,
            'gene_symbol': self.gene_symbol,
            'gene_name': self.gene_name,
            'chromosome': self.chromosome,
            'position': self.position,
            'reference_base': self.reference_base,
            'alternate_base': self.alternate_base,
            'impact': self.impact
        }

    @staticmethod
    def from_request(data):
        return {
            'gene_id': data.get('gene_id'),
            'chromosome': data.get('chromosome'),
            'position': data.get('position'),
            'reference_base': data.get('reference_base'),
            'alternate_base': data.get('alternate_base'),
            'impact': data.get('impact')
        }

    @staticmethod
    def validate_data(data):
        errors = []

        if not data.get('gene_id'):
            errors.append('gene_id is required')
        if not data.get('chromosome'):
            errors.append('chromosome is required')
        if not data.get('position'):
            errors.append('position is required')
        if not data.get('reference_base'):
            errors.append('reference_base is required')
        if not data.get('alternate_base'):
            errors.append('alternate_base is required')
        if not data.get('impact'):
            errors.append('impact is required')

        return (len(errors) == 0, errors)