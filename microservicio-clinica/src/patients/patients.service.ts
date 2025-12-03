import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Patient } from './entities/patient.entity';
import { CreatePatientDto, UpdatePatientDto } from './dto';
import { IPatientsService } from './interfaces';
import { PatientNotFoundException } from './exceptions';
//
@Injectable()
export class PatientsService implements IPatientsService {
    constructor(
        @InjectRepository(Patient)
        private readonly patientRepository: Repository<Patient>,
    ) {}

    // Listar todos los pacientes
    async findAll(): Promise<Patient[]> {
        return await this.patientRepository.find();
    }

    // Buscar un paciente por ID
    async findOne(id: string): Promise<Patient> {
        const patient = await this.patientRepository.findOne({ where: { id } });

        if (!patient) {
            throw new PatientNotFoundException(id);
        }

        return patient;
    }

    // Crear un nuevo paciente
    async create(createPatientDto: CreatePatientDto): Promise<Patient> {
        // Crear instancia de Patient
        const patient = this.patientRepository.create(createPatientDto);

        // Guardar en la BD
        return await this.patientRepository.save(patient);
    }

    // Actualizar un paciente
    async update(id: string, updatePatientDto: UpdatePatientDto): Promise<Patient> {
        // Verificar que el paciente existe
        const patient = await this.findOne(id);

        // Actualizar campos
        Object.assign(patient, updatePatientDto);

        // Guardar cambios
        return await this.patientRepository.save(patient);
    }

    // Eliminar un paciente (soft delete - cambiar status)
    async remove(id: string): Promise<void> {
        // Verificar que el paciente existe
        const patient = await this.findOne(id);

        // Cambiar status a Inactivo
        patient.status = 'Inactivo';

        // Guardar cambio
        await this.patientRepository.save(patient);
    }
}