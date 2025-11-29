from abc import ABC, abstractmethod


class IPatientVariantReportService(ABC):
    """Interfaz para el servicio de reportes"""

    @abstractmethod
    def get_all_reports(self):
        pass

    @abstractmethod
    def get_report_by_id(self, report_id):
        pass

    @abstractmethod
    def get_reports_by_patient(self, patient_id):
        pass

    @abstractmethod
    def create_report(self, report_data):
        pass

    @abstractmethod
    def update_report(self, report_id, report_data):
        pass

    @abstractmethod
    def delete_report(self, report_id):
        pass