from datetime import datetime

class Venta:
    def __init__(self, id_venta, id_usuario, nombre_usuario, id_producto, nombre_producto, 
                 cantidad, fecha=None):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "id_producto": self.id_producto,
            "nombre_producto": self.nombre_producto,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["id_venta"],
            datos["id_usuario"],
            datos["nombre_usuario"],
            datos["id_producto"],
            datos["nombre_producto"],
            datos["cantidad"],
            datos["fecha"]
        )