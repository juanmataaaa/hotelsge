# 🏨 HotelSGE - Gestión de Reservas de Hotel

Aplicación desarrollada en **Odoo** para la gestión simplificada de reservas de hotel. Este módulo permite administrar clientes, habitaciones, reservas y valoraciones de forma estructurada y eficiente.

## 📌 Descripción

**HotelSGE** es un módulo personalizado de Odoo diseñado para cubrir las necesidades básicas de gestión hotelera. Incluye funcionalidades clave como:

* Gestión de clientes
* Administración de habitaciones
* Creación y control de reservas
* Sistema de valoraciones por parte de los clientes

## 🚀 Funcionalidades

### 👤 Clientes

* Registro de clientes con:

  * Nombre
  * Email (único)
  * Teléfono
* Relación con reservas realizadas

### 🛏️ Habitaciones

* Tipos de habitación:

  * Simple
  * Doble
  * Suite
* Estado de la habitación:

  * Libre
  * Ocupada

### 📅 Reservas

* Asociación a cliente
* Fechas de entrada y salida
* Generación automática de código de reserva
* Validaciones de fechas

### ⭐ Valoraciones

* Relación entre cliente y reserva
* Sistema de puntuación (1 a 5 estrellas)
* Validaciones para asegurar coherencia de datos

## 🧱 Estructura del Proyecto

```
hotelsge/
│
├── models/
│   ├── cliente.py
│   ├── habitacion.py
│   ├── reserva.py
│   └── HotelReview.py
│
├── views/
│   ├── cliente.xml
│   ├── habitacion.xml
│   ├── reserva.xml
│   ├── review.xml
│   ├── menus.xml
│   └── actions.xml
│
├── security/
│   └── ir.model.access.csv
│
├── demo/
│   └── demo.xml
│
└── __manifest__.py
```

## ⚙️ Instalación

1. Copia el módulo en la carpeta de addons de Odoo:

   ```bash
   cp -r hotelsge /ruta/a/odoo/addons/
   ```

2. Reinicia el servidor de Odoo

3. Activa el modo desarrollador

4. Actualiza la lista de aplicaciones

5. Instala el módulo **HotelSGE**

## 🛠️ Tecnologías utilizadas

* Python
* Odoo Framework
* XML (vistas)
* PostgreSQL

## 📈 Posibles mejoras

* Gestión de disponibilidad avanzada
* Facturación automática
* Integración con pagos
* Panel de estadísticas
* API REST

## 👨‍💻 Autor

**Juan Mata**
