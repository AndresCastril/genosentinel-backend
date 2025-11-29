from abc import ABC, abstractmethod


class IGeneticVariantService(ABC):
    """Interfaz para el servicio de variantes"""

    @abstractmethod
    def get_all_variants(self):
        pass

    @abstractmethod
    def get_variant_by_id(self, variant_id):
        pass

    @abstractmethod
    def get_variants_by_gene(self, gene_id):
        pass

    @abstractmethod
    def create_variant(self, variant_data):
        pass

    @abstractmethod
    def update_variant(self, variant_id, variant_data):
        pass

    @abstractmethod
    def delete_variant(self, variant_id):
        pass