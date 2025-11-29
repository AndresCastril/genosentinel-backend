import { Controller, Get, Post, Put, Delete, Body, Param, HttpCode, HttpStatus } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';
import { TumorTypesService } from './tumor-types.service';
import { CreateTumorTypeDto, UpdateTumorTypeDto } from './dto';

@ApiTags('tumor-types')
@Controller('tumor-types')
export class TumorTypesController {
    constructor(private readonly tumorTypesService: TumorTypesService) {}

    @Get()
    @ApiOperation({ summary: 'Listar todos los tipos de tumor' })
    @ApiResponse({ status: 200, description: 'Lista de tipos de tumor obtenida exitosamente' })
    async findAll() {
        return await this.tumorTypesService.findAll();
    }

    @Get(':id')
    @ApiOperation({ summary: 'Obtener un tipo de tumor por ID' })
    @ApiResponse({ status: 200, description: 'Tipo de tumor encontrado' })
    @ApiResponse({ status: 404, description: 'Tipo de tumor no encontrado' })
    async findOne(@Param('id') id: string) {
        return await this.tumorTypesService.findOne(+id);
    }

    @Post()
    @ApiOperation({ summary: 'Crear un nuevo tipo de tumor' })
    @ApiResponse({ status: 201, description: 'Tipo de tumor creado exitosamente' })
    @ApiResponse({ status: 400, description: 'Datos inválidos' })
    async create(@Body() createTumorTypeDto: CreateTumorTypeDto) {
        return await this.tumorTypesService.create(createTumorTypeDto);
    }

    @Put(':id')
    @ApiOperation({ summary: 'Actualizar un tipo de tumor' })
    @ApiResponse({ status: 200, description: 'Tipo de tumor actualizado' })
    @ApiResponse({ status: 404, description: 'Tipo de tumor no encontrado' })
    async update(
        @Param('id') id: string,
        @Body() updateTumorTypeDto: UpdateTumorTypeDto,
    ) {
        return await this.tumorTypesService.update(+id, updateTumorTypeDto);
    }

    @Delete(':id')
    @HttpCode(HttpStatus.NO_CONTENT)
    @ApiOperation({ summary: 'Eliminar un tipo de tumor' })
    @ApiResponse({ status: 204, description: 'Tipo de tumor eliminado' })
    @ApiResponse({ status: 404, description: 'Tipo de tumor no encontrado' })
    async remove(@Param('id') id: string) {
        await this.tumorTypesService.remove(+id);
    }
}
//