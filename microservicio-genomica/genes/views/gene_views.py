from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..services import GeneService
from ..dtos import GeneDTO


class GeneListView(APIView):
    """Controlador para listar y crear genes"""

    def __init__(self):
        super().__init__()
        self.gene_service = GeneService()

    @swagger_auto_schema(
        operation_description="Obtener lista de todos los genes",
        responses={200: "Lista de genes obtenida exitosamente"}
    )
    def get(self, request):
        """GET /genes/ - Listar todos los genes"""
        # Obtener genes del servicio
        genes = self.gene_service.get_all_genes()

        # Convertir a DTOs
        genes_dto = [GeneDTO(gene).to_dict() for gene in genes]

        return Response(genes_dto, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Crear un nuevo gen",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['symbol', 'full_name', 'function_summary'],
            properties={
                'symbol': openapi.Schema(type=openapi.TYPE_STRING, description='Símbolo del gen'),
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre completo del gen'),
                'function_summary': openapi.Schema(type=openapi.TYPE_STRING, description='Resumen de función'),
            }
        ),
        responses={
            201: "Gen creado exitosamente",
            400: "Datos inválidos"
        }
    )
    def post(self, request):
        """POST /genes/ - Crear un nuevo gen"""
        # Extraer datos del request
        gene_data = GeneDTO.from_request(request.data)

        # Crear gen usando el servicio
        gene = self.gene_service.create_gene(gene_data)

        # Convertir a DTO y retornar
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_201_CREATED)


class GeneDetailView(APIView):
    """Controlador para ver, actualizar y eliminar un gen específico"""

    def __init__(self):
        super().__init__()
        self.gene_service = GeneService()

    @swagger_auto_schema(
        operation_description="Obtener un gen por ID",
        responses={
            200: "Gen encontrado",
            404: "Gen no encontrado"
        }
    )
    def get(self, request, pk):
        """GET /genes/{id}/ - Obtener un gen por ID"""
        # Buscar gen por ID
        gene = self.gene_service.get_gene_by_id(pk)

        # Convertir a DTO
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Actualizar un gen existente",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'symbol': openapi.Schema(type=openapi.TYPE_STRING),
                'full_name': openapi.Schema(type=openapi.TYPE_STRING),
                'function_summary': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: "Gen actualizado",
            404: "Gen no encontrado",
            400: "Datos inválidos"
        }
    )
    def put(self, request, pk):
        """PUT /genes/{id}/ - Actualizar un gen"""
        # Extraer datos
        gene_data = GeneDTO.from_request(request.data)

        # Actualizar usando el servicio
        gene = self.gene_service.update_gene(pk, gene_data)

        # Retornar gen actualizado
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Eliminar un gen",
        responses={
            204: "Gen eliminado",
            404: "Gen no encontrado"
        }
    )
    def delete(self, request, pk):
        """DELETE /genes/{id}/ - Eliminar un gen"""
        # Eliminar usando el servicio
        self.gene_service.delete_gene(pk)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """PATCH /genes/{id}/ - Actualización parcial de un gen"""
        gene = self.gene_service.get_gene_by_id(pk)

        # Solo actualizar los campos que vengan en el request
        if 'symbol' in request.data:
            gene.symbol = request.data['symbol']
        if 'full_name' in request.data:
            gene.full_name = request.data['full_name']
        if 'function_summary' in request.data:
            gene.function_summary = request.data['function_summary']

        gene.save()
        gene_dto = GeneDTO(gene).to_dict()
        return Response(gene_dto, status=status.HTTP_200_OK)