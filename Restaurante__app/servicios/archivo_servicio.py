import json
import os
from modelos import Usuario, Producto, Venta

class RestauranteServicio:
    def __init__(self):
        self.usuarios = self._cargar_usuarios()
        self.productos = self._cargar_productos()
        self.ventas = self._cargar_ventas()

    # ===== USUARIOS =====
    def _cargar_usuarios(self):
        ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "usuarios.json")
        if not os.path.exists(ruta): return []
        with open(ruta, "r", encoding="utf-8") as f:
            return [Usuario.from_dict(u) for u in json.load(f)]

    def _guardar_usuarios(self):
        ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "usuarios.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in self.usuarios], f, ensure_ascii=False, indent=4)

    def validar_login(self, usuario, contrasena):
        for u in self.usuarios:
            if u.usuario == usuario and u.contrasena == contrasena:
                return True, u
        return False, None

    def obtener_usuarios(self): return self.usuarios
    def buscar_usuario(self, identificador):
        return next((u for u in self.usuarios if u.identificador == identificador), None)

    # ===== PRODUCTOS =====
    def _cargar_productos(self):
        ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "productos.json")
        if not os.path.exists(ruta): return []
        with open(ruta, "r", encoding="utf-8") as f:
            return [Producto.from_dict(p) for p in json.load(f)]

    def _guardar_productos(self):
        ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "productos.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.productos], f, ensure_ascii=False, indent=4)

    def obtener_productos(self): return self.productos
    def buscar_producto(self, id_producto):
        return next((p for p in self.productos if p.id == id_producto), None)

    def agregar_producto(self, nombre, precio, cantidad):
        nuevo_id = max([p.id for p in self.productos], default=0) + 1
        self.productos.append(Producto(nuevo_id, nombre, precio, cantidad))
        self._guardar_productos()
        return True

    def actualizar_producto(self, id_producto, nombre, precio, cantidad):
        prod = self.buscar_producto(id_producto)
        if prod:
            prod.nombre, prod.precio, prod.cantidad = nombre, float(precio), int(cantidad)
            self._guardar_productos()
            return True
        return False

    def eliminar_producto(self, id_producto):
        prod = self.buscar_producto(id_producto)
        if prod:
            self.productos.remove(prod)
            self._guardar_productos()
            return True
        return False

    # ===== VENTAS — SEMANA 15 =====
    def _cargar_ventas(self):
        ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "ventas.json")
        if not os.path.exists(ruta): return []
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    def _guardar_ventas(self, ventas):
        ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "ventas.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(ventas, f, ensure_ascii=False, indent=4)

    def registrar_venta(self, id_usuario, id_producto, cantidad):
        usuario = self.buscar_usuario(id_usuario)
        producto = self.buscar_producto(id_producto)
        if not usuario: return False, "Usuario no encontrado"
        if not producto: return False, "Producto no encontrado"
        if cantidad <= 0: return False, "Cantidad debe ser mayor a cero"
        if producto.cantidad < cantidad: return False, f"Stock insuficiente: {producto.cantidad}"

        ventas = self._cargar_ventas()
        nuevo_id = max([v["id_venta"] for v in ventas], default=0) + 1
        venta = Venta(nuevo_id, usuario.identificador, usuario.nombre,
                      producto.id, producto.nombre, cantidad)

        producto.cantidad -= cantidad
        self.actualizar_producto(producto.id, producto.nombre, producto.precio, producto.cantidad)

        ventas.append(venta.to_dict())
        self._guardar_ventas(ventas)
        self.ventas = ventas
        return True, f"Venta registrada. ID: {nuevo_id}"

    def obtener_ventas(self):
        return [Venta.from_dict(v) for v in self._cargar_ventas()]