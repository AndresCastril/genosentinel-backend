from rest_framework import serializers
from .models import Gene, GeneticVariant, PatientVariantReport


class GeneSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Gene.
    Expone todos los campos del gen.
    """
    class Meta:
        model = Gene
        fields = ['id', 'symbol', 'full_name', 'function_summary']
        read_only_fields = ['id']


class GeneticVariantSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo GeneticVariant.
    Incluye información del gen relacionado.
    """
    gene_symbol = serializers.CharField(source='gene.symbol', read_only=True)
    gene_name = serializers.CharField(source='gene.full_name', read_only=True)

    class Meta:
        model = GeneticVariant
        fields = [
            'id', 'gene', 'gene_symbol', 'gene_name',
            'chromosome', 'position', 'reference_base',
            'alternate_base', 'impact'
        ]
        read_only_fields = ['id']


class GeneticVariantDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado para GeneticVariant.
    Incluye todos los datos del gen relacionado (nested).
    """
    gene = GeneSerializer(read_only=True)

    class Meta:
        model = GeneticVariant
        fields = [
            'id', 'gene', 'chromosome', 'position',
            'reference_base', 'alternate_base', 'impact'
        ]
        read_only_fields = ['id']


class PatientVariantReportSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo PatientVariantReport.
    Incluye información básica de la variante.
    """
    variant_info = serializers.CharField(source='variant.__str__', read_only=True)
    gene_symbol = serializers.CharField(source='variant.gene.symbol', read_only=True)

    class Meta:
        model = PatientVariantReport
        fields = [
            'id', 'patient_id', 'variant', 'variant_info',
            'gene_symbol', 'detection_date', 'allele_frequency'
        ]
        read_only_fields = ['id']

    def validate_allele_frequency(self, value):
        """
        Valida que la frecuencia alélica esté entre 0 y 1.
        """
        if value < 0 or value > 1:
            raise serializers.ValidationError(
                "Allele frequency must be between 0 and 1"
            )
        return value


class PatientVariantReportDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado para PatientVariantReport.
    Incluye todos los datos de la variante (nested).
    """
    variant = GeneticVariantDetailSerializer(read_only=True)

    class Meta:
        model = PatientVariantReport
        fields = [
            'id', 'patient_id', 'variant',
            'detection_date', 'allele_frequency'
        ]
        read_only_fields = ['id']