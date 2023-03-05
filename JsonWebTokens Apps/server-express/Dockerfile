# Establece la imagen base
FROM node:latest

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . ./

# Instala las dependencias
RUN npm install

# Expone el puerto de la aplicación
EXPOSE 3000

# Ejecuta la aplicación
# CMD ["node", "index.js"]
ENTRYPOINT ["tail", "-f", "/dev/null"]