class GeneDTO:
    """DTO para genes"""

    def __init__(self, gene):
        # Copiamos los datos del modelo al DTO
        self.id = gene.id
        self.symbol = gene.symbol
        self.full_name = gene.full_name
        self.function_summary = gene.function_summary

    def to_dict(self):
        # Convertimos a diccionario para el JSON
        return {
            'id': self.id,
            'symbol': self.symbol,
            'full_name': self.full_name,
            'function_summary': self.function_summary
        }

    @staticmethod
    def from_request(data):
        # Sacamos los datos del request
        return {
            'symbol': data.get('symbol'),
            'full_name': data.get('full_name'),
            'function_summary': data.get('function_summary')
        }

    @staticmethod
    def validate_data(data):
        # Validamos que vengan todos los campos
        errors = []

        if not data.get('symbol'):
            errors.append('symbol is required')
        if not data.get('full_name'):
            errors.append('full_name is required')
        if not data.get('function_summary'):
            errors.append('function_summary is required')

        return (len(errors) == 0, errors)