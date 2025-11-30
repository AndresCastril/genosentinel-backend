import { IsString, IsNotEmpty, IsDateString, IsOptional, MaxLength } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';

export class CreatePatientDto {
    @ApiProperty({
        description: 'ID del paciente (UUID)',
        example: 'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(36)
    id: string;

    @ApiProperty({
        description: 'Nombre del paciente',
        example: 'Juan',
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(100)
    firstName: string;

    @ApiProperty({
        description: 'Apellido del paciente',
        example: 'Pérez',
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(100)
    lastName: string;

    @ApiProperty({
        description: 'Fecha de nacimiento (YYYY-MM-DD)',
        example: '1980-05-15',
    })
    @IsDateString()
    @IsNotEmpty()
    birthDate: string;

    @ApiProperty({
        description: 'Género del paciente',
        example: 'M',
        enum: ['M', 'F'],
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(20)
    gender: string;

    @ApiProperty({
        description: 'Estado del paciente',
        example: 'Activo',
        enum: ['Activo', 'Seguimiento', 'Inactivo'],
        required: false,
    })
    @IsString()
    @IsOptional()
    @MaxLength(20)
    status?: string;
}
//