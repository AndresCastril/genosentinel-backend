from ..models import Gene
from ..exceptions import GeneNotFoundException, InvalidGeneDataException
from ..dtos import GeneDTO
from .interfaces.igene_service import IGeneService


class GeneService(IGeneService):
    """Servicio para manejar la lógica de genes"""

    def get_all_genes(self):
        # Traer todos los genes de la BD
        return Gene.objects.all()

    def get_gene_by_id(self, gene_id):
        # Buscar un gen por ID, si no existe lanzar excepción
        try:
            return Gene.objects.get(id=gene_id)
        except Gene.DoesNotExist:
            raise GeneNotFoundException()

    def create_gene(self, gene_data):
        # Validar datos antes de crear
        is_valid, errors = GeneDTO.validate_data(gene_data)
        if not is_valid:
            raise InvalidGeneDataException(detail=errors)

        # Crear y guardar el gen
        gene = Gene(**gene_data)
        gene.save()
        return gene

    def update_gene(self, gene_id, gene_data):
        # Buscar el gen
        gene = self.get_gene_by_id(gene_id)

        # Validar datos
        is_valid, errors = GeneDTO.validate_data(gene_data)
        if not is_valid:
            raise InvalidGeneDataException(detail=errors)

        # Actualizar campos
        gene.symbol = gene_data.get('symbol', gene.symbol)
        gene.full_name = gene_data.get('full_name', gene.full_name)
        gene.function_summary = gene_data.get('function_summary', gene.function_summary)
        gene.save()

        return gene

    def delete_gene(self, gene_id):
        # Buscar y eliminar
        gene = self.get_gene_by_id(gene_id)
        gene.delete()