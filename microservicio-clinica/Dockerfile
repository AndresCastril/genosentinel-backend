# Imagen base de Node.js
FROM node:18-alpine

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el código fuente
COPY . .

# Compilar la aplicación TypeScript
RUN npm run build

# Exponer el puerto 3000
EXPOSE 3000

# Variables de entorno (se pueden sobrescribir al ejecutar)
ENV DB_HOST=localhost
ENV DB_PORT=3306
ENV DB_USERNAME=root
ENV DB_PASSWORD=andres54
ENV DB_DATABASE=genosentinel
ENV PORT=3000
ENV NODE_ENV=production

CMD ["node", "dist/main"]