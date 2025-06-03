# Plenitas Devices API (Test Project)

A REST API built with Django and the Django Rest Framework that allows:

- User registration using email as username
- Authentication using JWT (JSON Web Tokens)
- Device management by authenticated user
- Interactive documentation using Swagger/OpenAPI (drf-spectacular)

---

## Requirements

- Python 3.10+
- pip
- Virtualenv (optional but recommended)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/tu_usuario/django-devices-api.git
cd plenitas
```

2. **Create and activate a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate
```

6. **Run the server:**

```bash
python manage.py runserver
```

---

## JWT Authentication

Authentication is done using JWT tokens using `djangorestframework-simplejwt`.

### 1. Get access token:

```
POST /api/token/
```

**Body:**

```json
{
  "email": "johndoe@example.com",
  "password": "your_password"
}
```

### 2. Refresh the token:

```
POST /api/token/refresh/
```

---

## Available endpoints

| Method | URL                   | Description                            | Authentication |
|--------|-----------------------|----------------------------------------|------------|
| POST   | `/api/register/`      | Registro de usuario                    | No         |
| POST   | `/api/token/`         | Obtener token JWT                      | No         |
| POST   | `/api/token/refresh/` | Refrescar token JWT                    | No         |
| GET    | `/api/devices/`       | Listar dispositivos del usuario actual | Sí         |
| POST   | `/api/devices/`       | Crear nuevo dispositivo                | Sí         |

---

## API Doc (Swagger / OpenAPI)

Once the server is running, access the interactive documentation at:

- Swagger UI:  
  `http://127.0.0.1:8000/api/schema/swagger-ui/`

- Esquema JSON:  
  `http://127.0.0.1:8000/api/schema/`

---

## Used technologies

- Django 5.x
- Django Rest Framework
- JWT (djangorestframework-simplejwt)
- Swagger/OpenAPI (drf-spectacular)

---

## Example of use: Create a device

1. Get token with `/api/token/`
2. Authorize in Swagger ("Authorize" button)
3. Go to `POST /api/devices/`
4. Send:

```json
{
  "name": "Test server",
  "ip": "192.168.1.10",
  "is_active": true
}
```

Response:

```json
{
  "id": 1,
  "name": "Test server",
  "ip": "192.168.1.10",
  "is_active": true,
  "user_email": "johndoe@example.com"
}
```

---

## Tests

This project includes automated testing using **pytest** and the **Django REST Framework** to ensure proper functioning of the authentication and device management endpoints.

### How to run the tests

1. Make sure you have `pytest` installed and the project dependencies.
2. Run the tests with the following command:

```bash
pytest
```

---

## Author

Developed by [Erick M. Hernández Quiñones] · [erickmhq@gmail.com]