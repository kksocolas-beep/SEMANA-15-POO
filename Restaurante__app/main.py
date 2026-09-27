import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.servicio = RestauranteServicio()
        self.usuario_actual = None
        self._mostrar_login()

    def _mostrar_login(self):
        self._limpiar_ventana()
        LoginView(self.root, self.servicio, self._mostrar_main)

    def _mostrar_main(self, usuario=None):
        self.usuario_actual = usuario
        self._limpiar_ventana()
        MainView(self.root, self.servicio, self._mostrar_login, self.usuario_actual)

    def _limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()