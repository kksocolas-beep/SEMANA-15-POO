# Restaurante App — Semana 15: Manejo de Eventos y Gestión de Ventas

## Tema
Ampliación de la aplicación de restaurante incorporando el registro de ventas mediante manejo básico de eventos, delegación de lógica de negocio al servicio y persistencia en archivos JSON.

## Objetivo
Comprender los fundamentos del manejo de eventos en interfaces gráficas: acción del usuario → botón (command=) → callback → servicio → persistencia → respuesta visual. Desarrollar una nueva sección de Ventas que relacione usuarios y productos, manteniendo la arquitectura modular y la separación de responsabilidades.

## Arquitectura

Restaurante/
├── assets/
├── datos/ # Almacenamiento en JSON
│ ├── productos.json
│ ├── usuarios.json
│ └── ventas.json # Historial de ventas
├── modelos/ # Clases de datos
│ ├── producto.py
│ ├── usuario.py
│ └── venta.py # Modelo de Venta
├── servicios/ # Lógica de negocio
│ └── restaurante_servicio.py
├── ui/ # Interfaces gráficas
│ ├── login_view.py
│ └── main_view.py
├── main.py # Punto de entrada
└── README.md


## Flujo de Eventos — Semana 15
Usuario hace clic en "Registrar Venta"
↓
command= → _callback_registrar_venta()
↓
Obtiene selecciones de la interfaz
↓
Delegar a RestauranteServicio.registrar_venta()
↓
Validar usuario + producto + stock
↓
Descontar del inventario
↓
Guardar en ventas.json
↓
Actualizar tabla de ventas
↓
Mostrar mensaje de éxito al usuario


## Características
- 🔐 Inicio de sesión con validación
- 🏠 Panel principal con resumen
- 👤 Gestión de Usuarios
- 📦 Gestión de Productos
- 💰 **Gestión de Ventas:**
  - Selección de usuario mediante Combobox
  - Selección de producto mediante Combobox
  - Validación de stock disponible
  - Descuento automático de inventario
  - Registro con fecha y hora
  - Tabla histórica de ventas
  - Persistencia en ventas.json
- 🎨 Interfaz moderna con menú lateral
- 🖼️ Carpeta `assets/` con logotipo del sistema

## Credenciales de acceso
- **Usuario:** `admin` — **Contraseña:** `1234`
- **Usuario:** `cajero` — **Contraseña:** `5678`

## Requisitos
- Python 3.10+
- Tkinter (incluido en Python)
- No requiere librerías externas

## Ejecución
```bash
python main.py

Guía de Uso — Ventas
En el menú lateral, haz clic en "💰 Ventas"
Selecciona un Usuario de la lista desplegable
Selecciona un Producto de la lista desplegable
Ingresa la Cantidad a vender
Haz clic en "💰 Registrar Venta"
✅ El sistema valida, descuenta del stock, guarda y actualiza la tabla automáticamente
Las ventas quedan guardadas en datos/ventas.json y se cargan al reiniciar la aplicación

Notas Técnicas
La lógica de negocio está en RestauranteServicio, NO en la interfaz
El callback solo coordina, no procesa reglas
Los datos se persisten automáticamente en archivos JSON
Se valida existencia de usuario, producto y stock antes de vender
El ID de venta se genera automáticamente
Autor
Desarrollado para la asignatura de Programación Orientada a Objetos
Semana 15 — Manejo de Eventos
Ecuador

→ Usuario: admin | Contraseña: 1234