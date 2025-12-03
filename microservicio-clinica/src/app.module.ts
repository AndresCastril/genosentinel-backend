import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PatientsModule } from './patients/patients.module';
import { TumorTypesModule } from './tumor-types/tumor-types.module';
import { ClinicalRecordsModule } from './clinical-records/clinical-records.module';

@Module({
    imports: [
        // Configuración de variables de entorno
        ConfigModule.forRoot({
            isGlobal: true,
            envFilePath: '.env',
        }),

        // Configuración de TypeORM (MySQL)
        TypeOrmModule.forRoot({
            type: 'mysql',
            host: process.env.DB_HOST,
            port: parseInt(process.env.DB_PORT || '3306', 10),
            username: process.env.DB_USERNAME,
            password: process.env.DB_PASSWORD,
            database: process.env.DB_DATABASE,
            entities: [__dirname + '/**/*.entity{.ts,.js}'],
            synchronize: true,
            logging: process.env.NODE_ENV === 'development',
        }),

        PatientsModule,

        TumorTypesModule,

        ClinicalRecordsModule,
    ],
    controllers: [AppController],
    providers: [AppService],
})
export class AppModule {}
//