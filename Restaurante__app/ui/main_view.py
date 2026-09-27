import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, root, servicio, callback_cerrar_sesion, usuario_actual=None):
        self.root = root
        self.servicio = servicio
        self.callback_cerrar_sesion = callback_cerrar_sesion
        self.usuario_actual = usuario_actual
        self.root.title("🍽️ Sistema de Gestión — Restaurante")
        self.root.geometry("1100x700")
        self.root.configure(bg="#f1f5f9")
        self._construir_interfaz()
        self._mostrar_inicio()

    def _construir_interfaz(self):
        top = tk.Frame(self.root, bg="#1e3a8a", height=60)
        top.pack(fill=tk.X, side=tk.TOP)
        top.pack_propagate(False)
        tk.Label(top, text="🍽️ Sistema de Gestión — Restaurante", font=("Segoe UI", 16, "bold"), bg="#1e3a8a", fg="white").pack(side=tk.LEFT, padx=20, pady=15)
        tk.Label(top, text=f"👤 {self.usuario_actual.nombre if self.usuario_actual else 'Usuario'}", font=("Segoe UI", 10), bg="#1e3a8a", fg="#bfdbfe").pack(side=tk.RIGHT, padx=10)
        tk.Button(top, text="Cerrar Sesión", command=self.callback_cerrar_sesion, bg="#dc2626", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=15, pady=5, cursor="hand2").pack(side=tk.RIGHT, padx=15)

        self.menu = tk.Frame(self.root, bg="#ffffff", width=220)
        self.menu.pack(fill=tk.Y, side=tk.LEFT)
        self.menu.pack_propagate(False)
        tk.Frame(self.menu, bg="#e2e8f0", height=2).pack(fill=tk.X, padx=10, pady=10)

        self._btn_menu("🏠 Inicio", self._mostrar_inicio)
        self._btn_menu("👤 Usuarios", self._mostrar_usuarios)
        self._btn_menu("🍽️ Productos", self._mostrar_productos)
        self._btn_menu("💰 Ventas", self._mostrar_ventas)

        tk.Frame(self.menu, bg="#e2e8f0", height=2).pack(fill=tk.X, padx=10, pady=10)
        tk.Frame(self.menu, bg="#ffffff").pack(expand=True, fill=tk.BOTH)

        self.contenido = tk.Frame(self.root, bg="#f8fafc")
        self.contenido.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def _btn_menu(self, texto, cmd):
        tk.Button(self.menu, text=texto, command=cmd, bg="#ffffff", fg="#334155", font=("Segoe UI", 11), relief="flat", cursor="hand2", anchor="w", padx=15, pady=10).pack(fill=tk.X, padx=15, pady=5)

    def _limpiar(self):
        for w in self.contenido.winfo_children(): w.destroy()

    def _mostrar_inicio(self):
        self._limpiar()
        tk.Label(self.contenido, text="¡Bienvenido al Sistema de Gestión del Restaurante!", font=("Segoe UI", 22, "bold"), bg="#f8fafc", fg="#1e293b").pack(pady=(40,20))
        tk.Label(self.contenido, text="Seleccione una opción del menú lateral para comenzar.", font=("Segoe UI", 13), bg="#f8fafc", fg="#64748b").pack(pady=10)
        stats = tk.Frame(self.contenido, bg="#f8fafc")
        stats.pack(pady=40)
        self._tarjeta(stats, "Productos", len(self.servicio.obtener_productos()), "#dbeafe", "#1e40af")
        self._tarjeta(stats, "Usuarios", len(self.servicio.obtener_usuarios()), "#dcfce7", "#166534")
        self._tarjeta(stats, "Ventas", len(self.servicio.obtener_ventas()), "#fef3c7", "#92400e")

    def _tarjeta(self, padre, titulo, valor, c1, c2):
        f = tk.Frame(padre, bg=c1, padx=30, pady=25)
        f.pack(side=tk.LEFT, padx=15)
        tk.Label(f, text=titulo, font=("Segoe UI", 12), bg=c1, fg=c2).pack()
        tk.Label(f, text=str(valor), font=("Segoe UI", 28, "bold"), bg=c1, fg=c2).pack(pady=10)

    def _mostrar_usuarios(self):
        self._limpiar()
        tk.Label(self.contenido, text="Gestión de Usuarios", font=("Segoe UI", 20, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0,20))
        marco = tk.Frame(self.contenido, bg="#ffffff", padx=10, pady=10)
        marco.pack(fill=tk.BOTH, expand=True)
        t = ttk.Treeview(marco, columns=("id", "nombre", "usuario", "rol"), show="headings", height=15)
        for col, w in [("id",80),("nombre",250),("usuario",200),("rol",150)]:
            t.heading(col, text=col.title())
            t.column(col, width=w)
        t.pack(fill=tk.BOTH, expand=True)
        for u in self.servicio.obtener_usuarios():
            t.insert("", tk.END, values=(u.identificador, u.nombre, u.usuario, u.rol))

    def _mostrar_productos(self):
        self._limpiar()
        tk.Label(self.contenido, text="Gestión de Productos", font=("Segoe UI", 20, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0,20))
        form = tk.LabelFrame(self.contenido, text="Datos del Producto", font=("Segoe UI", 11, "bold"), padx=15, pady=15, bg="#ffffff")
        form.pack(fill=tk.X, pady=(0,20))

        tk.Label(form, text="Nombre:", font=("Segoe UI", 10), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        self.var_nom = tk.StringVar()
        tk.Entry(form, textvariable=self.var_nom, width=30).grid(row=0, column=1, padx=10)
        tk.Label(form, text="Precio:", font=("Segoe UI", 10), bg="#ffffff").grid(row=0, column=2, sticky="w", pady=5)
        self.var_pre = tk.StringVar()
        tk.Entry(form, textvariable=self.var_pre, width=15).grid(row=0, column=3, padx=10)
        tk.Label(form, text="Cantidad:", font=("Segoe UI", 10), bg="#ffffff").grid(row=0, column=4, sticky="w", pady=5)
        self.var_can = tk.StringVar()
        tk.Entry(form, textvariable=self.var_can, width=15).grid(row=0, column=5, padx=10)

        btns = tk.Frame(form, bg="#ffffff")
        btns.grid(row=1, column=0, columnspan=6, pady=15)
        tk.Button(btns, text="Agregar", command=self._agregar_prod, bg="#22c55e", fg="white", font=("Segoe UI",10,"bold"), relief="flat", padx=20, cursor="hand2").pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="Eliminar Seleccionado", command=self._eliminar_prod, bg="#ef4444", fg="white", font=("Segoe UI",10,"bold"), relief="flat", padx=20, cursor="hand2").pack(side=tk.LEFT, padx=5)

        marco = tk.Frame(self.contenido, bg="#ffffff", padx=10, pady=10)
        marco.pack(fill=tk.BOTH, expand=True)
        self.tabla_prod = ttk.Treeview(marco, columns=("id", "nombre", "precio", "cantidad"), show="headings", height=12)
        for col, w in [("id",60),("nombre",300),("precio",120),("cantidad",120)]:
            self.tabla_prod.heading(col, text=col.title())
            self.tabla_prod.column(col, width=w)
        self.tabla_prod.pack(fill=tk.BOTH, expand=True)
        self._refrescar_prod()

    def _refrescar_prod(self):
        for i in self.tabla_prod.get_children(): self.tabla_prod.delete(i)
        for p in self.servicio.obtener_productos():
            self.tabla_prod.insert("", tk.END, values=(p.id, p.nombre, f"${p.precio:.2f}", p.cantidad))

    def _agregar_prod(self):
        n, p, c = self.var_nom.get().strip(), self.var_pre.get().strip(), self.var_can.get().strip()
        if not n or not p or not c: messagebox.showwarning("Aviso", "Complete todos los campos"); return
        if not p.replace(".","",1).isdigit() or not c.isdigit(): messagebox.showwarning("Aviso", "Precio y cantidad deben ser números"); return
        self.servicio.agregar_producto(n, float(p), int(c))
        messagebox.showinfo("Éxito", "Producto agregado")
        self.var_nom.set(""); self.var_pre.set(""); self.var_can.set("")
        self._refrescar_prod()

    def _eliminar_prod(self):
        sel = self.tabla_prod.selection()
        if not sel: messagebox.showwarning("Aviso", "Seleccione un producto"); return
        idp = self.tabla_prod.item(sel[0])["values"][0]
        if messagebox.askyesno("Confirmar", "¿Eliminar producto?"):
            self.servicio.eliminar_producto(idp)
            self._refrescar_prod()
            messagebox.showinfo("Éxito", "Producto eliminado")

    def _mostrar_ventas(self):
        self._limpiar()
        tk.Label(self.contenido, text="Gestión de Ventas", font=("Segoe UI", 20, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0,20))
        cont = tk.Frame(self.contenido, bg="#f8fafc")
        cont.pack(fill=tk.BOTH, expand=True)

        form = tk.LabelFrame(cont, text="Registrar Venta", font=("Segoe UI", 11, "bold"), padx=15, pady=15, bg="#ffffff")
        form.pack(side=tk.LEFT, fill=tk.Y, padx=(0,20))

        tk.Label(form, text="Usuario:", font=("Segoe UI", 10), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=8)
        self.combo_usr = ttk.Combobox(form, state="readonly", width=30)
        self.combo_usr.grid(row=0, column=1, pady=8)
        self._cargar_combos_usr()

        tk.Label(form, text="Producto:", font=("Segoe UI", 10), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=8)
        self.combo_prod = ttk.Combobox(form, state="readonly", width=30)
        self.combo_prod.grid(row=1, column=1, pady=8)
        self._cargar_combos_prod()

        tk.Label(form, text="Cantidad:", font=("Segoe UI", 10), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=8)
        self.var_cant_venta = tk.StringVar()
        tk.Entry(form, textvariable=self.var_cant_venta, font=("Segoe UI", 10), width=33).grid(row=2, column=1, pady=8)

        tk.Button(form, text="💰 Registrar Venta", command=self._callback_venta,
                  bg="#2563eb", fg="white", font=("Segoe UI", 11, "bold"),
                  relief="flat", pady=10, cursor="hand2").grid(row=3, column=0, columnspan=2, sticky="ew", pady=(25,10))

        tabla_frm = tk.LabelFrame(cont, text="Ventas Registradas", font=("Segoe UI", 11, "bold"), padx=10, pady=10, bg="#ffffff")
        tabla_frm.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tabla_ventas = ttk.Treeview(tabla_frm, columns=("id", "usuario", "producto", "cantidad", "fecha"), show="headings", height=15)
        for col, w in [("id",60),("usuario",150),("producto",150),("cantidad",80),("fecha",150)]:
            self.tabla_ventas.heading(col, text=col.title())
            self.tabla_ventas.column(col, width=w)
        self.tabla_ventas.pack(fill=tk.BOTH, expand=True)
        self._refrescar_ventas()

    def _cargar_combos_usr(self):
        vals = [f"{u.identificador} - {u.nombre}" for u in self.servicio.obtener_usuarios()]
        self.combo_usr["values"] = vals
        if vals: self.combo_usr.current(0)

    def _cargar_combos_prod(self):
        vals = [f"{p.id} - {p.nombre}" for p in self.servicio.obtener_productos()]
        self.combo_prod["values"] = vals
        if vals: self.combo_prod.current(0)

    def _callback_venta(self):
        sel_usr = self.combo_usr.get()
        sel_prod = self.combo_prod.get()
        cant = self.var_cant_venta.get().strip()
        if not sel_usr or not sel_prod: messagebox.showwarning("Aviso", "Seleccione usuario y producto"); return
        if not cant.isdigit(): messagebox.showwarning("Aviso", "Cantidad debe ser número"); return
        idu = int(sel_usr.split(" - ")[0])
        idp = int(sel_prod.split(" - ")[0])
        c = int(cant)
        ok, msg = self.servicio.registrar_venta(idu, idp, c)
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.var_cant_venta.set("")
            self._cargar_combos_prod()
            self._refrescar_ventas()
        else:
            messagebox.showerror("Error", msg)

    def _refrescar_ventas(self):
        for i in self.tabla_ventas.get_children(): self.tabla_ventas.delete(i)
        for v in self.servicio.obtener_ventas():
            self.tabla_ventas.insert("", tk.END, values=(v.id_venta, v.nombre_usuario, v.nombre_producto, v.cantidad, v.fecha))