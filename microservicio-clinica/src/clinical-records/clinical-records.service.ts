import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ClinicalRecord } from './entities/clinical-record.entity';
import { CreateClinicalRecordDto, UpdateClinicalRecordDto } from './dto';
import { IClinicalRecordsService } from './interfaces';
import { ClinicalRecordNotFoundException } from './exceptions';
import { PatientsService } from '../patients/patients.service';
import { TumorTypesService } from '../tumor-types/tumor-types.service';

@Injectable()
export class ClinicalRecordsService implements IClinicalRecordsService {
    constructor(
        @InjectRepository(ClinicalRecord)
        private readonly clinicalRecordRepository: Repository<ClinicalRecord>,
        private readonly patientsService: PatientsService,
        private readonly tumorTypesService: TumorTypesService,
    ) {}

    // Listar todas las historias clínicas
    async findAll(): Promise<ClinicalRecord[]> {
        return await this.clinicalRecordRepository.find({
            relations: ['patient', 'tumorType'],
        });
    }

    // Buscar historias clínicas por paciente
    async findByPatient(patientId: string): Promise<ClinicalRecord[]> {
        // Verificar que el paciente existe
        await this.patientsService.findOne(patientId);

        return await this.clinicalRecordRepository.find({
            where: { patientId },
            relations: ['patient', 'tumorType'],
        });
    }

    // Buscar una historia clínica por ID
    async findOne(id: string): Promise<ClinicalRecord> {
        const record = await this.clinicalRecordRepository.findOne({
            where: { id },
            relations: ['patient', 'tumorType'],
        });

        if (!record) {
            throw new ClinicalRecordNotFoundException(id);
        }

        return record;
    }

    // Crear una nueva historia clínica
    async create(createClinicalRecordDto: CreateClinicalRecordDto): Promise<ClinicalRecord> {
        // Validar que el paciente existe
        await this.patientsService.findOne(createClinicalRecordDto.patientId);

        // Validar que el tipo de tumor existe
        await this.tumorTypesService.findOne(createClinicalRecordDto.tumorTypeId);

        // Crear la historia clínica
        const record = this.clinicalRecordRepository.create(createClinicalRecordDto);
        return await this.clinicalRecordRepository.save(record);
    }

    // Actualizar una historia clínica
    async update(id: string, updateClinicalRecordDto: UpdateClinicalRecordDto): Promise<ClinicalRecord> {
        // Verificar que la historia clínica existe
        const record = await this.findOne(id);

        // Si se cambia el paciente, validar que existe
        if (updateClinicalRecordDto.patientId) {
            await this.patientsService.findOne(updateClinicalRecordDto.patientId);
        }

        // Si se cambia el tipo de tumor, validar que existe
        if (updateClinicalRecordDto.tumorTypeId) {
            await this.tumorTypesService.findOne(updateClinicalRecordDto.tumorTypeId);
        }

        // Actualizar campos
        Object.assign(record, updateClinicalRecordDto);

        return await this.clinicalRecordRepository.save(record);
    }

    // Eliminar una historia clínica
    async remove(id: string): Promise<void> {
        const record = await this.findOne(id);
        await this.clinicalRecordRepository.remove(record);
    }
}
//