# iFruitScraping

Aplicación para recoger información.
## Instalación y Ejecución

### Con Docker

1. **Requisitos previos**:
   - Docker instalado en tu sistema.

2. **Clona el repositorio**:
   ```bash
   git clone https://github.com/JuanFalHqz/iFruitScraping.git
3. **Construye la imagen**
   
   En este caso la imagen se puede llamar scraping_app.
   ```bash
   docker build -t scraping_app .
4. **Ejecuta el contenedor**
   ```bash
   docker run -d -p 8000:8000 scraping_app 

La aplicación estará disponible en http://localhost:8000.

**Saludos**
