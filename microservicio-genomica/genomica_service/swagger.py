from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="GenoSentinel - Microservicio Genómica",
        default_version='v1',
        description="""
API REST para gestión de información genómica de pacientes oncológicos.

Este microservicio maneja:
- Catálogo de genes de interés oncológico
- Registro de variantes genéticas (mutaciones)
- Reportes de variantes por paciente
        """,
        contact=openapi.Contact(email="andresd.castrilllont@autonoma.edu.co"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)