import { TumorType } from '../entities/tumor-type.entity';
import { CreateTumorTypeDto, UpdateTumorTypeDto } from '../dto';

export interface ITumorTypesService {
    // Listar todos los tipos de tumor
    findAll(): Promise<TumorType[]>;

    // Buscar un tipo de tumor por ID
    findOne(id: number): Promise<TumorType>;

    // Crear un nuevo tipo de tumor
    create(createTumorTypeDto: CreateTumorTypeDto): Promise<TumorType>;

    // Actualizar un tipo de tumor existente
    update(id: number, updateTumorTypeDto: UpdateTumorTypeDto): Promise<TumorType>;

    // Eliminar un tipo de tumor
    remove(id: number): Promise<void>;
}