from django.contrib import admin
from django.urls import path, include, re_path
from .swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genes.urls')),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

