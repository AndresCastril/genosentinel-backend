import { ClinicalRecord } from '../entities/clinical-record.entity';
import { CreateClinicalRecordDto, UpdateClinicalRecordDto } from '../dto';

export interface IClinicalRecordsService {
    // Listar todas las historias clínicas
    findAll(): Promise<ClinicalRecord[]>;

    // Buscar historias clínicas por paciente
    findByPatient(patientId: string): Promise<ClinicalRecord[]>;

    // Buscar una historia clínica por ID
    findOne(id: string): Promise<ClinicalRecord>;

    // Crear una nueva historia clínica
    create(createClinicalRecordDto: CreateClinicalRecordDto): Promise<ClinicalRecord>;

    // Actualizar una historia clínica existente
    update(id: string, updateClinicalRecordDto: UpdateClinicalRecordDto): Promise<ClinicalRecord>;

    // Eliminar una historia clínica
    remove(id: string): Promise<void>;
}