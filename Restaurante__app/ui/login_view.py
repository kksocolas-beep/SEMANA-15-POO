import tkinter as tk
from tkinter import ttk, messagebox

class LoginView:
    def __init__(self, root, servicio, callback_exito):
        self.root = root
        self.servicio = servicio
        self.callback_exito = callback_exito
        
        self.root.title("Restaurante - Tkinter")
        self.root.geometry("420x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#fef3c7")
        
        self._construir_interfaz()

    def _construir_interfaz(self):
        marco = tk.Frame(self.root, bg="#fef3c7", padx=40, pady=30)
        marco.pack(expand=True, fill="both")

        # 🍽️ LOGO — igual a tu imagen
        icono = tk.Label(
            marco,
            text="🍽️",
            font=("Segoe UI", 72),
            bg="#fef3c7",
            fg="#2563eb"
        )
        icono.pack(pady=(0, 10))

        tk.Label(
            marco,
            text="RESTAURANTE",
            font=("Segoe UI", 22, "bold"),
            bg="#fef3c7",
            fg="#1e293b"
        ).pack(pady=(0, 5))

        tk.Label(
            marco,
            text="Inicio de sesión",
            font=("Segoe UI", 12),
            bg="#fef3c7",
            fg="#64748b"
        ).pack(pady=(0, 35))

        tk.Label(marco, text="Usuario", font=("Segoe UI", 10),
                 bg="#fef3c7", fg="#334155", anchor="w").pack(fill="x")
        self.entry_usuario = ttk.Entry(marco, font=("Segoe UI", 12))
        self.entry_usuario.pack(fill="x", pady=(5, 20))
        self.entry_usuario.insert(0, "")

        tk.Label(marco, text="Contraseña", font=("Segoe UI", 10),
                 bg="#fef3c7", fg="#334155", anchor="w").pack(fill="x")
        self.entry_contrasena = ttk.Entry(marco, font=("Segoe UI", 12), show="•")
        self.entry_contrasena.pack(fill="x", pady=(5, 30))

        tk.Button(
            marco,
            text="Iniciar Sesión",
            command=self._login,
            font=("Segoe UI", 13, "bold"),
            bg="#2563eb",
            fg="white",
            relief="flat",
            cursor="hand2",
            height=1,
            width=25
        ).pack(pady=(0, 10))

        self.entry_usuario.focus()
        self.root.bind("<Return>", lambda e: self._login())

    def _login(self):
        usuario = self.entry_usuario.get().strip()
        contrasena = self.entry_contrasena.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning("Aviso", "Complete todos los campos")
            return

        ok, datos_usuario = self.servicio.validar_login(usuario, contrasena)
        
        if ok:
            self.callback_exito(datos_usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")