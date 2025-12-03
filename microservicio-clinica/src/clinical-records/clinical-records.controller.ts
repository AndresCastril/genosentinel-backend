import { Controller, Get, Post, Put, Delete, Body, Param, Query, HttpCode, HttpStatus } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiQuery } from '@nestjs/swagger';
import { ClinicalRecordsService } from './clinical-records.service';
import { CreateClinicalRecordDto, UpdateClinicalRecordDto } from './dto';

@ApiTags('clinical-records')
@Controller('clinical-records')
export class ClinicalRecordsController {
    constructor(private readonly clinicalRecordsService: ClinicalRecordsService) {}

    @Get()
    @ApiOperation({ summary: 'Listar historias clínicas (filtro opcional por paciente)' })
    @ApiQuery({ name: 'patient_id', required: false, description: 'ID del paciente para filtrar' })
    @ApiResponse({ status: 200, description: 'Lista de historias clínicas obtenida exitosamente' })
    async findAll(@Query('patient_id') patientId?: string) {
        if (patientId) {
            return await this.clinicalRecordsService.findByPatient(patientId);
        }
        return await this.clinicalRecordsService.findAll();
    }

    @Get(':id')
    @ApiOperation({ summary: 'Obtener una historia clínica por ID' })
    @ApiResponse({ status: 200, description: 'Historia clínica encontrada' })
    @ApiResponse({ status: 404, description: 'Historia clínica no encontrada' })
    async findOne(@Param('id') id: string) {
        return await this.clinicalRecordsService.findOne(id);
    }

    @Post()
    @ApiOperation({ summary: 'Crear una nueva historia clínica' })
    @ApiResponse({ status: 201, description: 'Historia clínica creada exitosamente' })
    @ApiResponse({ status: 400, description: 'Datos inválidos' })
    @ApiResponse({ status: 404, description: 'Paciente o tipo de tumor no encontrado' })
    async create(@Body() createClinicalRecordDto: CreateClinicalRecordDto) {
        return await this.clinicalRecordsService.create(createClinicalRecordDto);
    }

    @Put(':id')
    @ApiOperation({ summary: 'Actualizar una historia clínica' })
    @ApiResponse({ status: 200, description: 'Historia clínica actualizada' })
    @ApiResponse({ status: 404, description: 'Historia clínica no encontrada' })
    async update(
        @Param('id') id: string,
        @Body() updateClinicalRecordDto: UpdateClinicalRecordDto,
    ) {
        return await this.clinicalRecordsService.update(id, updateClinicalRecordDto);
    }
//
    @Delete(':id')
    @HttpCode(HttpStatus.NO_CONTENT)
    @ApiOperation({ summary: 'Eliminar una historia clínica' })
    @ApiResponse({ status: 204, description: 'Historia clínica eliminada' })
    @ApiResponse({ status: 404, description: 'Historia clínica no encontrada' })
    async remove(@Param('id') id: string) {
        await this.clinicalRecordsService.remove(id);
    }
}