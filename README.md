# FastAPI Products API

Este proyecto proporciona una API RESTful simple para gestionar productos. Está diseñada para integrarse fácilmente con aplicaciones frontend como Angular o React, y en particular con la app **Angular 20 Course App** desarrollada por el profesor Alejandro Alzate.

## Tecnologías

- Python 3.10+
- FastAPI
- Pydantic
- CORS Middleware
- Uvicorn (para desarrollo local)

## Endpoints disponibles

| Método | Ruta                        | Descripción                        |
|--------|-----------------------------|------------------------------------|
| GET    | `/api/products`            | Lista todos los productos          |
| POST   | `/api/products`            | Crea un nuevo producto             |

## Modelo de datos

```
{
  "id": 1,
  "name": "Producto 1",
  "price": 99.99
}
```

## Instalación
### Crear entorno virtual
bash
Copiar
Editar
python -m venv env
```
source env/bin/activate  # En Windows: env\Scripts\activate
```

### Instalar dependencias

```
pip install fastapi uvicorn
```

### Ejecutar el servidor

```
uvicorn main:app --reload
```

El servidor estará disponible en: http://localhost:8000

### Probar en Swagger UI
Puedes probar todos los endpoints en:

```
http://localhost:8000/docs
```
