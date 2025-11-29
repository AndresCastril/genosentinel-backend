from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import GeneService
from ..dtos import GeneDTO


class GeneListView(APIView):
    """Listar y crear genes"""

    def __init__(self):
        super().__init__()
        self.gene_service = GeneService()

    def get(self, request):
        """GET /genes/ - Listar todos los genes"""
        genes = self.gene_service.get_all_genes()
        genes_dto = [GeneDTO(gene).to_dict() for gene in genes]
        return Response(genes_dto, status=status.HTTP_200_OK)

    def post(self, request):
        """POST /genes/ - Crear un nuevo gen"""
        gene_data = GeneDTO.from_request(request.data)
        gene = self.gene_service.create_gene(gene_data)
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_201_CREATED)


class GeneDetailView(APIView):
    """Ver, actualizar y eliminar un gen específico"""

    def __init__(self):
        super().__init__()
        self.gene_service = GeneService()

    def get(self, request, pk):
        """GET /genes/{id}/ - Obtener un gen por ID"""
        gene = self.gene_service.get_gene_by_id(pk)
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """PUT /genes/{id}/ - Actualizar un gen"""
        gene_data = GeneDTO.from_request(request.data)
        gene = self.gene_service.update_gene(pk, gene_data)
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """DELETE /genes/{id}/ - Eliminar un gen"""
        self.gene_service.delete_gene(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)