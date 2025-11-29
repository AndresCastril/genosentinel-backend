import { Patient } from '../entities/patient.entity';
import { CreatePatientDto, UpdatePatientDto } from '../dto';

export interface IPatientsService {
    // Listar todos los pacientes
    findAll(): Promise<Patient[]>;

    // Buscar un paciente por ID
    findOne(id: string): Promise<Patient>;

    // Crear un nuevo paciente
    create(createPatientDto: CreatePatientDto): Promise<Patient>;

    // Actualizar un paciente existente
    update(id: string, updatePatientDto: UpdatePatientDto): Promise<Patient>;

    // Eliminar un paciente (soft delete - cambiar status a Inactivo)
    remove(id: string): Promise<void>;
}