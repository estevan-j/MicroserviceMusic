# MicroserviceMusic API

Una API REST para gestión de música construida con Flask, siguiendo arquitectura de microservicios con separación de capas.

## 🎵 Características

- **API REST completa**: Endpoints CRUD para gestión de canciones
- **Arquitectura en capas**: Routes, Services, Repository y Models
- **Validación robusta**: Pydantic para validación de datos tipados
- **ORM avanzado**: SQLAlchemy con modelos relacionales
- **Containerización**: Docker y CI/CD con GitHub Actions
- **Documentación**: Schemas bien definidos para request/response

## 📁 Estructura del Proyecto

```
MicroserviceMusic/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias Python
├── .env                           # Variables de entorno
├── Dockerfile                     # Configuración Docker
├── .github/workflows/             # GitHub Actions CI/CD
│   └── docker-deploy.yml
├── config/
│   ├── __init__.py
│   └── database.py               # Configuración centralizada de DB
├── models/
│   ├── __init__.py
│   └── song.py                   # Modelo de datos Song
├── schemas/
│   ├── __init__.py
│   └── song_schema.py            # Validación Pydantic
├── repository/
│   ├── __init__.py
│   └── song_repository.py        # Acceso a datos
├── services/
│   ├── __init__.py
│   └── song_service.py           # Lógica de negocio
├── routes/
│   ├── __init__.py
│   └── song_routes.py            # Endpoints HTTP
└── dev.db                        # Base de datos SQLite
```

## 🚀 Inicio Rápido

### 1. Configurar Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación

```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

## 🎼 Endpoints de la API

### Health Check
- `GET /api/test` - Verificar estado de la API

### Gestión de Canciones
- `GET /api/songs` - Obtener todas las canciones
- `POST /api/songs` - Crear una nueva canción
- `PUT /api/songs/{id}` - Actualizar una canción
- `DELETE /api/songs/{id}` - Eliminar una canción

### Búsqueda y Filtros
- `GET /api/songs/search?name=query` - Buscar canciones por nombre
- `GET /api/songs/popular?limit=10` - Obtener canciones más populares
- `POST /api/songs/{id}/play` - Incrementar contador de reproducciones

## 📋 Ejemplos de Uso

### Crear Canción
```bash
curl -X POST http://localhost:5000/api/songs \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bohemian Rhapsody",
    "url": "https://spotify.com/track/123",
    "plays": 1000000
  }'
```

### Obtener Canciones
```bash
curl http://localhost:5000/api/songs
```

### Buscar Canciones
```bash
curl "http://localhost:5000/api/songs/search?name=bohemian"
```

### Incrementar Reproducciones
```bash
curl -X POST http://localhost:5000/api/songs/1/play
```

## 📊 Modelos de Datos

### SongSchema (Request - POST)
```json
{
  "name": "string (1-200 chars)",
  "url": "string (1-500 chars)",
  "plays": "integer >= 0 (opcional, default: 0)"
}
```

### SongUpdateSchema (Request - PUT)
```json
{
  "name": "string (1-200 chars, opcional)",
  "url": "string (1-500 chars, opcional)"
}
```

### SongResponseSchema (Response)
```json
{
  "id": 1,
  "name": "Bohemian Rhapsody",
  "url": "https://spotify.com/track/123",
  "plays": 1500000,
  "created_at": "2025-01-17T15:30:45.123456",
  "updated_at": "2025-01-17T16:45:30.789012"
}
```

## 🔧 Variables de Entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `FLASK_APP` | Archivo principal | `app.py` |
| `FLASK_ENV` | Entorno Flask | `development` |
| `SECRET_KEY` | Clave secreta | `dev-secret-key` |
| `DATABASE_URL` | URL de base de datos | `sqlite:///dev.db` |
| `PORT` | Puerto del servidor | `5000` |

## 🏗️ Arquitectura

### Stack Tecnológico
El proyecto utiliza **Flask** como framework web de Python con **Flask-CORS** y **Flask-SQLAlchemy**, implementando **Pydantic** para validación automática de datos mediante schemas tipados. La persistencia se maneja con **SQLAlchemy** como ORM conectado a **SQLite** para desarrollo, mientras que la organización del código se estructura usando **Blueprints de Flask** para lograr modularidad y escalabilidad en la arquitectura de la API REST.

### Patrón de Capas
- **Routes (Controladores)**: Manejan endpoints HTTP y validación de entrada
- **Services (Lógica de Negocio)**: Coordinan operaciones y transforman datos
- **Repository (Acceso a Datos)**: Abstraen operaciones de base de datos
- **Models (Entidades)**: Definen estructura de datos con SQLAlchemy

## 🐳 Containerización

### Ejecutar con Docker
```bash
# Construir imagen
docker build -t microservice-music .

# Ejecutar contenedor
docker run -p 5000:5000 microservice-music
```

### Docker Compose
```bash
docker-compose up --build
```

## 🚀 CI/CD con GitHub Actions

El proyecto incluye pipeline automático que:
- **Construye** imagen Docker en cada push
- **Ejecuta** tests automáticos
- **Despliega** a DockerHub desde branch main
- **Escanea** vulnerabilidades de seguridad

## 🧪 Testing

### Ejecutar Tests
```bash
# Test básico de la API
curl -f http://localhost:5000/api/test

# Test con Docker
docker run --rm -p 5000:5000 microservice-music &
sleep 5
curl -f http://localhost:5000/api/test
```

## 🔧 Desarrollo

### Añadir Nuevos Endpoints

1. **Crear route** en `routes/song_routes.py`
2. **Implementar lógica** en `services/song_service.py`
3. **Añadir operaciones** en `repository/song_repository.py`

### Añadir Validaciones

```python
# En schemas/song_schema.py
class NewSchema(BaseModel):
    field: str = Field(..., min_length=1, max_length=100)
```

## 📦 Tecnologías Utilizadas

- **Flask 2.3.3**: Framework web
- **Pydantic 2.5.0**: Validación de datos
- **SQLAlchemy 2.0.23**: ORM
- **Flask-SQLAlchemy 3.0.5**: Integración SQLAlchemy
- **Flask-CORS 4.0.0**: Manejo de CORS

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una feature branch (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la branch (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.