import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TumorTypesController } from './tumor-types.controller';
import { TumorTypesService } from './tumor-types.service';
import { TumorType } from './entities/tumor-type.entity';

@Module({
    imports: [
        TypeOrmModule.forFeature([TumorType]),
    ],
    controllers: [TumorTypesController],
    providers: [TumorTypesService],
    exports: [TumorTypesService],
})
export class TumorTypesModule {}

//