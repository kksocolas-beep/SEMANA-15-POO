class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["id"],
            datos["nombre"],
            datos["precio"],
            datos["cantidad"]
        )