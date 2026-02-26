# NexCore ERP Engine 🚀

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

NexCore es un motor de backend modular diseñado para sistemas de planificación de recursos empresariales (ERP). Este proyecto aplica **Arquitectura Limpia** y una separación estricta entre el Core del negocio y la interfaz de usuario.

## 🛠 Arquitectura y Tecnologías
- **Backend:** Django 4.2+ & Django REST Framework (DRF).
- **Base de Datos:** PostgreSQL (Producción) / MySQL compatible.
- **Infraestructura:** Docker & Docker Compose para orquestación de servicios.
- **Estilo de Código:** PEP8, principios SOLID y DRY.

## 📂 Estructura del Proyecto
El proyecto utiliza una estructura desacoplada:
- `/backend`: Lógica de negocio y API.
  - `/apps`: Aplicaciones modulares (Users, Products, Inventory).
  - `/core`: Configuración central del sistema.
- `/frontend`: Aplicación cliente (desacoplada).

## 🚀 Instalación y Uso (Docker)

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/NexCore-ERP-Engine.git](https://github.com/tu-usuario/NexCore-ERP-Engine.git)
   cd NexCore-ERP-Engine