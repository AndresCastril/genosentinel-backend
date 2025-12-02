import { IsString, IsNotEmpty, IsDateString, IsInt, MaxLength } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';
//
export class CreateClinicalRecordDto {
    @ApiProperty({
        description: 'ID del paciente',
        example: 'patient-001',
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(36)
    patientId: string;

    @ApiProperty({
        description: 'ID del tipo de tumor',
        example: 1,
    })
    @IsInt()
    @IsNotEmpty()
    tumorTypeId: number;

    @ApiProperty({
        description: 'Fecha de diagnóstico (YYYY-MM-DD)',
        example: '2024-01-15',
    })
    @IsDateString()
    @IsNotEmpty()
    diagnosisDate: string;

    @ApiProperty({
        description: 'Etapa del cáncer',
        example: 'IIA',
        enum: ['I', 'IA', 'IB', 'II', 'IIA', 'IIB', 'III', 'IIIA', 'IIIB', 'IIIC', 'IV'],
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(10)
    stage: string;

    @ApiProperty({
        description: 'Protocolo de tratamiento',
        example: 'Quimioterapia + Radioterapia',
    })
    @IsString()
    @IsNotEmpty()
    treatmentProtocol: string;
}