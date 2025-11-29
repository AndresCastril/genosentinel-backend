import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ClinicalRecordsController } from './clinical-records.controller';
import { ClinicalRecordsService } from './clinical-records.service';
import { ClinicalRecord } from './entities/clinical-record.entity';
import { PatientsModule } from '../patients/patients.module';
import { TumorTypesModule } from '../tumor-types/tumor-types.module';

@Module({
    imports: [
        TypeOrmModule.forFeature([ClinicalRecord]),
        PatientsModule,      // Importar para usar PatientsService
        TumorTypesModule,    // Importar para usar TumorTypesService
    ],
    controllers: [ClinicalRecordsController],
    providers: [ClinicalRecordsService],
    exports: [ClinicalRecordsService],
})
export class ClinicalRecordsModule {}
//