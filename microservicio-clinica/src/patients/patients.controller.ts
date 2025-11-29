import { Controller, Get, Post, Put, Delete, Body, Param, HttpCode, HttpStatus } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';
import { PatientsService } from './patients.service';
import { CreatePatientDto, UpdatePatientDto } from './dto';

@ApiTags('patients')
@Controller('patients')
export class PatientsController {
    constructor(private readonly patientsService: PatientsService) {}

    @Get()
    @ApiOperation({ summary: 'Listar todos los pacientes' })
    @ApiResponse({ status: 200, description: 'Lista de pacientes obtenida exitosamente' })
    async findAll() {
        return await this.patientsService.findAll();
    }

    @Get(':id')
    @ApiOperation({ summary: 'Obtener un paciente por ID' })
    @ApiResponse({ status: 200, description: 'Paciente encontrado' })
    @ApiResponse({ status: 404, description: 'Paciente no encontrado' })
    async findOne(@Param('id') id: string) {
        return await this.patientsService.findOne(id);
    }

    @Post()
    @ApiOperation({ summary: 'Crear un nuevo paciente' })
    @ApiResponse({ status: 201, description: 'Paciente creado exitosamente' })
    @ApiResponse({ status: 400, description: 'Datos inválidos' })
    async create(@Body() createPatientDto: CreatePatientDto) {
        return await this.patientsService.create(createPatientDto);
    }

    @Put(':id')
    @ApiOperation({ summary: 'Actualizar un paciente' })
    @ApiResponse({ status: 200, description: 'Paciente actualizado' })
    @ApiResponse({ status: 404, description: 'Paciente no encontrado' })
    async update(
        @Param('id') id: string,
        @Body() updatePatientDto: UpdatePatientDto,
    ) {
        return await this.patientsService.update(id, updatePatientDto);
    }
//
    @Delete(':id')
    @HttpCode(HttpStatus.NO_CONTENT)
    @ApiOperation({ summary: 'Desactivar un paciente' })
    @ApiResponse({ status: 204, description: 'Paciente desactivado' })
    @ApiResponse({ status: 404, description: 'Paciente no encontrado' })
    async remove(@Param('id') id: string) {
        await this.patientsService.remove(id);
    }
}