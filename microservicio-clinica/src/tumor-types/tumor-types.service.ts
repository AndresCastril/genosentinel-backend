import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { TumorType } from './entities/tumor-type.entity';
import { CreateTumorTypeDto, UpdateTumorTypeDto } from './dto';
import { ITumorTypesService } from './interfaces';
import { TumorTypeNotFoundException } from './exceptions';

@Injectable()
export class TumorTypesService implements ITumorTypesService {
    constructor(
        @InjectRepository(TumorType)
        private readonly tumorTypeRepository: Repository<TumorType>,
    ) {}

    // Listar todos los tipos de tumor
    async findAll(): Promise<TumorType[]> {
        return await this.tumorTypeRepository.find();
    }

    // Buscar un tipo de tumor por ID
    async findOne(id: number): Promise<TumorType> {
        const tumorType = await this.tumorTypeRepository.findOne({ where: { id } });

        if (!tumorType) {
            throw new TumorTypeNotFoundException(id);
        }

        return tumorType;
    }

    // Crear un nuevo tipo de tumor
    async create(createTumorTypeDto: CreateTumorTypeDto): Promise<TumorType> {
        const tumorType = this.tumorTypeRepository.create(createTumorTypeDto);
        return await this.tumorTypeRepository.save(tumorType);
    }

    // Actualizar un tipo de tumor
    async update(id: number, updateTumorTypeDto: UpdateTumorTypeDto): Promise<TumorType> {
        const tumorType = await this.findOne(id);
        Object.assign(tumorType, updateTumorTypeDto);
        return await this.tumorTypeRepository.save(tumorType);
    }

    // Eliminar un tipo de tumor
    async remove(id: number): Promise<void> {
        const tumorType = await this.findOne(id);
        await this.tumorTypeRepository.remove(tumorType);
    }
}
//