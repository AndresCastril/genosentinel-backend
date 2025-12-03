from django.db import models
import uuid


class Gene(models.Model):
    """
    Catálogo de genes relevantes en oncología.
    Tabla: genes
    """
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255, db_column='full_name')
    function_summary = models.TextField(db_column='function_summary')

    class Meta:
        db_table = 'genes'
        managed = True

    def __str__(self):
        return self.symbol


class GeneticVariant(models.Model):
    """
    Registro de una mutación específica.
    Relación con Gen de Interés.
    Tabla: genetic_variants
    """
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    gene = models.ForeignKey(Gene, on_delete=models.RESTRICT, db_column='gene_id')
    chromosome = models.CharField(max_length=10)
    position = models.BigIntegerField()
    reference_base = models.CharField(max_length=100, db_column='reference_base')
    alternate_base = models.CharField(max_length=100, db_column='alternate_base')
    impact = models.CharField(max_length=50)

    class Meta:
        db_table = 'genetic_variants'
        managed = True

    def __str__(self):
        return f"{self.gene.symbol} - {self.chromosome}:{self.position}"


class PatientVariantReport(models.Model):
    """
    Librería de mutaciones encontradas en un paciente.
    Relación con Paciente (en microservicio Clínica) y Variante Genética.
    Tabla: patient_variant_reports
    """
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.CharField(max_length=36, db_column='patient_id')
    variant = models.ForeignKey(GeneticVariant, on_delete=models.RESTRICT, db_column='variant_id')
    detection_date = models.DateField(db_column='detection_date')
    allele_frequency = models.DecimalField(max_digits=5, decimal_places=4, db_column='allele_frequency')

    class Meta:
        db_table = 'patient_variant_reports'
        managed = True

    def __str__(self):
        return f"Patient {self.patient_id} - Variant {self.variant.id}"