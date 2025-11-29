import { IsString, IsNotEmpty, MaxLength } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';
//
export class CreateTumorTypeDto {
    @ApiProperty({
        description: 'Nombre del tipo de tumor',
        example: 'Cáncer de Mama',
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(150)
    name: string;

    @ApiProperty({
        description: 'Sistema afectado por el tumor',
        example: 'Glándulas Mamarias',
    })
    @IsString()
    @IsNotEmpty()
    @MaxLength(100)
    systemAffected: string;
}