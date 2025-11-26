from ..models import GeneticVariant
from ..exceptions import (
    GeneticVariantNotFoundException,
    InvalidVariantDataException,
    GeneNotFoundException
)
from ..dtos import GeneticVariantDTO
from .interfaces.igenetic_variant_service import IGeneticVariantService
from .gene_service import GeneService


class GeneticVariantService(IGeneticVariantService):
    """Servicio para manejar variantes genéticas"""

    def __init__(self):
        self.gene_service = GeneService()

    def get_all_variants(self):
        return GeneticVariant.objects.all()

    def get_variant_by_id(self, variant_id):
        try:
            return GeneticVariant.objects.get(id=variant_id)
        except GeneticVariant.DoesNotExist:
            raise GeneticVariantNotFoundException()

    def get_variants_by_gene(self, gene_id):
        # Verificar que el gen exista
        self.gene_service.get_gene_by_id(gene_id)

        # Filtrar variantes por gen
        return GeneticVariant.objects.filter(gene_id=gene_id)

    def create_variant(self, variant_data):
        # Validar datos
        is_valid, errors = GeneticVariantDTO.validate_data(variant_data)
        if not is_valid:
            raise InvalidVariantDataException(detail=errors)

        # Verificar que el gen exista
        gene_id = variant_data.get('gene_id')
        self.gene_service.get_gene_by_id(gene_id)

        # Crear variante
        variant = GeneticVariant(**variant_data)
        variant.save()
        return variant

    def update_variant(self, variant_id, variant_data):
        # Buscar variante
        variant = self.get_variant_by_id(variant_id)

        # Validar datos
        is_valid, errors = GeneticVariantDTO.validate_data(variant_data)
        if not is_valid:
            raise InvalidVariantDataException(detail=errors)

        # Si se cambia el gen, verificar que exista
        if 'gene_id' in variant_data:
            self.gene_service.get_gene_by_id(variant_data['gene_id'])

        # Actualizar campos
        variant.gene_id = variant_data.get('gene_id', variant.gene_id)
        variant.chromosome = variant_data.get('chromosome', variant.chromosome)
        variant.position = variant_data.get('position', variant.position)
        variant.reference_base = variant_data.get('reference_base', variant.reference_base)
        variant.alternate_base = variant_data.get('alternate_base', variant.alternate_base)
        variant.impact = variant_data.get('impact', variant.impact)
        variant.save()

        return variant

    def delete_variant(self, variant_id):
        variant = self.get_variant_by_id(variant_id)
        variant.delete()