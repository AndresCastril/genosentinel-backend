GenoSentinel

Sistema modular, seguro y escalable para la gestión y consulta de información genómica y clínica de pacientes oncológicos.

Descripción

GenoSentinel centraliza la información de variantes genéticas somáticas (librerías de mutaciones tumorales) y la vincula directamente con el historial clínico de pacientes oncológicos.

Arquitectura

- Microservicio de Autenticación/Gateway: Spring Boot (Puerto 8080)
- Microservicio Clínica**: NestJS (Puerto 3000)
- Microservicio Genómica**: Django (Puerto 8000)
- Base de Datos: MySQL



Clonar el Repositorio

git clone https://github.com/AndresCastril/genosentinel-backend.git
cd genosentinel-backend

Endpoints

- Autenticación: http://localhost:8080
- Clínica (Swagger): http://localhost:3000/api
- Genómica (Swagger): http://localhost:8000/swagger/

