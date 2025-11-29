import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { PatientsController } from './patients.controller';
import { PatientsService } from './patients.service';
import { Patient } from './entities/patient.entity';
//
@Module({
    imports: [
        TypeOrmModule.forFeature([Patient]), // Registrar la entidad
    ],
    controllers: [PatientsController],
    providers: [PatientsService],
    exports: [PatientsService], // Exportar para usar en otros módulos
})
export class PatientsModule {}