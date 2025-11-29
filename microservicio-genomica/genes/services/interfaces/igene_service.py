from abc import ABC, abstractmethod ## esto es lo que usamos para usar interfaces en python


class IGeneService(ABC):
    """Interfaz para el servicio de genes"""

    @abstractmethod
    def get_all_genes(self):
        pass

    @abstractmethod
    def get_gene_by_id(self, gene_id):
        pass

    @abstractmethod
    def create_gene(self, gene_data):
        pass

    @abstractmethod
    def update_gene(self, gene_id, gene_data):
        pass

    @abstractmethod
    def delete_gene(self, gene_id):
        pass