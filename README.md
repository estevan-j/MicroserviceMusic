# Flask API Project

Una API REST simple construida con Flask, Pydantic y SQLAlchemy para desarrollo.

## Características

- **Flask API REST**: Endpoints para operaciones CRUD
- **Pydantic**: Validación de datos de entrada y respuesta
- **SQLAlchemy**: ORM para manejo de base de datos
- **CORS**: Habilitado para requests cross-origin
- **SQLite**: Base de datos ligera para desarrollo
- **Configuración Simple**: Solo para ambiente de desarrollo

## Estructura del Proyecto

```
flask-api/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias Python
├── .env                   # Variables de entorno
├── README.md             # Este archivo
├── .gitignore            # Archivos a ignorar en git
└── dev.db                # Base de datos SQLite (se crea automáticamente)
```

## Inicio Rápido

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

## Endpoints de la API

### Health Check
- `GET /api/health` - Verificar estado de la API

### Usuarios
- `GET /api/users` - Obtener todos los usuarios
- `POST /api/users` - Crear un nuevo usuario
- `GET /api/users/{id}` - Obtener un usuario específico
- `PUT /api/users/{id}` - Actualizar un usuario
- `DELETE /api/users/{id}` - Eliminar un usuario

## Ejemplos de Uso

### Crear Usuario
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Juan Pérez", "email": "juan@email.com"}'
```

### Obtener Usuarios
```bash
curl http://localhost:5000/api/users
```

### Actualizar Usuario
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Juan Carlos"}'
```

## Modelos de Datos

### UserCreate (Request)
```json
{
  "name": "string",
  "email": "string"
}
```

### UserResponse
```json
{
  "id": 1,
  "name": "string",
  "email": "string",
  "created_at": "2025-01-01T12:00:00"
}
```

## Variables de Entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `FLASK_APP` | Archivo principal | `app.py` |
| `FLASK_ENV` | Entorno Flask | `development` |
| `SECRET_KEY` | Clave secreta | `dev-secret-key-for-development` |
| `DATABASE_URL` | URL de base de datos | `sqlite:///dev.db` |
| `PORT` | Puerto del servidor | `5000` |

## Desarrollo

### Añadir Nuevos Endpoints

Agrega nuevas rutas en `app.py`:

```python
@app.route('/api/new-endpoint', methods=['GET'])
def new_endpoint():
    return jsonify({'message': 'Nuevo endpoint'})
```

### Añadir Nuevos Modelos

1. **Modelo Pydantic** para validación:
```python
class NewModel(BaseModel):
    field: str
```

2. **Modelo SQLAlchemy** para base de datos:
```python
class NewTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(100), nullable=False)
```

## Tecnologías Utilizadas

- **Flask 3.0.0**: Framework web
- **Pydantic 2.5.0**: Validación de datos
- **SQLAlchemy 2.0.23**: ORM
- **Flask-SQLAlchemy 3.1.1**: Integración SQLAlchemy
- **Flask-CORS 4.0.0**: Manejo de CORS
- **python-dotenv 1.0.0**: Variables de entorno
