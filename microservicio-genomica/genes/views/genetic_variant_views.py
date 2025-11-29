from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import GeneticVariantService
from ..dtos import GeneticVariantDTO


class GeneticVariantListView(APIView):
    """Listar y crear variantes genéticas"""

    def __init__(self):
        super().__init__()
        self.variant_service = GeneticVariantService()

    def get(self, request):
        """GET /variants/ - Listar variantes (filtro opcional: ?gene_id=X)"""
        # Ver si viene filtro por gen
        gene_id = request.query_params.get('gene_id')

        if gene_id:
            variants = self.variant_service.get_variants_by_gene(gene_id)
        else:
            variants = self.variant_service.get_all_variants()

        variants_dto = [GeneticVariantDTO(variant).to_dict() for variant in variants]
        return Response(variants_dto, status=status.HTTP_200_OK)

    def post(self, request):
        """POST /variants/ - Crear una nueva variante"""
        variant_data = GeneticVariantDTO.from_request(request.data)
        variant = self.variant_service.create_variant(variant_data)
        variant_dto = GeneticVariantDTO(variant).to_dict()
        return Response(variant_dto, status=status.HTTP_201_CREATED)


class GeneticVariantDetailView(APIView):
    """Ver, actualizar y eliminar una variante específica"""

    def __init__(self):
        super().__init__()
        self.variant_service = GeneticVariantService()

    def get(self, request, pk):
        """GET /variants/{id}/ - Obtener una variante por ID"""
        variant = self.variant_service.get_variant_by_id(pk)
        variant_dto = GeneticVariantDTO(variant).to_dict()
        return Response(variant_dto, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """PUT /variants/{id}/ - Actualizar una variante"""
        variant_data = GeneticVariantDTO.from_request(request.data)
        variant = self.variant_service.update_variant(pk, variant_data)
        variant_dto = GeneticVariantDTO(variant).to_dict()
        return Response(variant_dto, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """DELETE /variants/{id}/ - Eliminar una variante"""
        self.variant_service.delete_variant(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """PATCH /variants/{id}/ - Actualización parcial"""
        variant = self.variant_service.get_variant_by_id(pk)

        if 'gene_id' in request.data:
            variant.gene_id = request.data['gene_id']
        if 'chromosome' in request.data:
            variant.chromosome = request.data['chromosome']
        if 'position' in request.data:
            variant.position = request.data['position']
        if 'reference_base' in request.data:
            variant.reference_base = request.data['reference_base']
        if 'alternate_base' in request.data:
            variant.alternate_base = request.data['alternate_base']
        if 'impact' in request.data:
            variant.impact = request.data['impact']

        variant.save()
        variant_dto = GeneticVariantDTO(variant).to_dict()
        return Response(variant_dto, status=status.HTTP_200_OK)