import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';
//
async function bootstrap() {
    const app = await NestFactory.create(AppModule);

    // Habilitar validación global
    app.useGlobalPipes(
        new ValidationPipe({
            whitelist: true,
            forbidNonWhitelisted: true,
            transform: true,
        }),
    );

    // Configurar CORS
    app.enableCors();

    // Configurar Swagger
    const config = new DocumentBuilder()
        .setTitle('GenoSentinel - Microservicio Clínica')
        .setDescription('API para gestión de pacientes, tipos de tumor e historias clínicas')
        .setVersion('1.0')
        .addTag('patients', 'Gestión de pacientes')
        .addTag('tumor-types', 'Catálogo de tipos de tumor')
        .addTag('clinical-records', 'Historias clínicas')
        .build();

    const document = SwaggerModule.createDocument(app, config);
    SwaggerModule.setup('swagger', app, document);

    const port = process.env.PORT || 3000;
    await app.listen(port);

    console.log(`Microservicio Clínica corriendo en: http://localhost:${port}`);
    console.log(`Swagger disponible en: http://localhost:${port}/swagger`);
}
bootstrap();