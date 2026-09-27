class Usuario:
    def __init__(self, identificador, nombre, usuario, contrasena, rol="usuario"):
        self.identificador = identificador
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["identificador"],
            datos["nombre"],
            datos["usuario"],
            datos["contrasena"],
            datos.get("rol", "usuario")
        )