import tkinter as tk
from tkinter import ttk, messagebox


# --------------------------
# CLASES DE MODELO
# --------------------------

class TipoPlaneta:
    """Clase que representa el tipo de planeta: gaseoso, terrestre o enano."""
    def __init__(self, id_planeta: int, tipo_planeta: str):
        self.id_planeta = id_planeta
        self.tipo_planeta = tipo_planeta

    def __str__(self):
        return self.tipo_planeta


class Planeta:
    """Clase principal que modela un planeta del sistema solar."""
    def __init__(self, nombre, satelites, masa, volumen, diametro, distancia_sol, tipo_planeta):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol  # en millones de km
        self.tipo_planeta = tipo_planeta

    def calcular_densidad(self):
        """Retorna la densidad del planeta: masa / volumen"""
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        """Determina si el planeta está más allá del cinturón de asteroides."""
        UA = self.distancia_sol * 1_000_000 / 149_597_870
        return UA > 3.4

    def mostrar_info(self):
        """Devuelve un resumen con los datos del planeta."""
        info = (
            f"🌎 Nombre: {self.nombre}\n"
            f"🛰 Satélites: {self.satelites}\n"
            f"⚖️ Masa: {self.masa:.2e} kg\n"
            f"📦 Volumen: {self.volumen:.2e} km³\n"
            f"📏 Diámetro: {self.diametro} km\n"
            f"🌞 Distancia al Sol: {self.distancia_sol} millones de km\n"
            f"🪐 Tipo: {self.tipo_planeta}\n"
            f"💠 Densidad: {self.calcular_densidad():.2e} kg/km³\n"
        )

        if self.es_planeta_exterior():
            info += "🚀 Este planeta es **EXTERIOR** al sistema solar.\n"
        else:
            info += "🌍 Este planeta es **INTERIOR** al sistema solar.\n"

        return info


# --------------------------
# INTERFAZ GRÁFICA
# --------------------------

class AppPlaneta:
    def __init__(self, root):
        self.root = root
        self.root.title("🌌 Registro de Planetas")
        self.root.geometry("520x630")
        self.root.resizable(False, False)

        # Variables
        self.vars = {
            "nombre": tk.StringVar(),
            "satelites": tk.StringVar(),
            "masa": tk.StringVar(),
            "volumen": tk.StringVar(),
            "diametro": tk.StringVar(),
            "distancia": tk.StringVar(),
        }

        self.tipo_var = tk.StringVar()

        # Diccionario de tipos de planeta
        self.tipos_planeta = {
            "Gaseoso": TipoPlaneta(1, "GASEOSO"),
            "Terrestre": TipoPlaneta(2, "TERRESTRE"),
            "Enano": TipoPlaneta(3, "ENANO"),
        }

        self.crear_interfaz()

    def crear_interfaz(self):
        marco = ttk.LabelFrame(self.root, text="Ingrese los datos del planeta 🌍", padding=12)
        marco.pack(padx=10, pady=10, fill="both", expand=True)

        etiquetas = ["Nombre", "Cantidad de satélites", "Masa (kg)",
                     "Volumen (km³)", "Diámetro (km)", "Distancia media al Sol (millones de km)"]

        for i, texto in enumerate(etiquetas):
            ttk.Label(marco, text=texto).grid(row=i, column=0, sticky="w", pady=5)
            ttk.Entry(marco, textvariable=self.vars[list(self.vars.keys())[i]], width=25).grid(row=i, column=1, pady=5)

        ttk.Label(marco, text="Tipo de planeta").grid(row=6, column=0, sticky="w", pady=5)
        ttk.Combobox(marco, textvariable=self.tipo_var,
                     values=list(self.tipos_planeta.keys()), width=22).grid(row=6, column=1, pady=5)

        ttk.Button(self.root, text="Registrar Planeta 🌠", command=self.crear_planeta).pack(pady=15)
        ttk.Button(self.root, text="Limpiar Campos 🧹", command=self.limpiar_campos).pack(pady=5)

        self.texto_salida = tk.Text(self.root, height=14, width=60, font=("Consolas", 10))
        self.texto_salida.pack(padx=10, pady=10)

    def crear_planeta(self):
        try:
            nombre = self.vars["nombre"].get()
            satelites = int(self.vars["satelites"].get())
            masa = float(self.vars["masa"].get())
            volumen = float(self.vars["volumen"].get())
            diametro = int(self.vars["diametro"].get())
            distancia = float(self.vars["distancia"].get())
            tipo = self.tipos_planeta[self.tipo_var.get()]

            planeta = Planeta(nombre, satelites, masa, volumen, diametro, distancia, tipo)

            self.texto_salida.delete(1.0, tk.END)
            self.texto_salida.insert(tk.END, planeta.mostrar_info())

            messagebox.showinfo("Éxito", "✅ Planeta registrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def limpiar_campos(self):
        for v in self.vars.values():
            v.set("")
        self.tipo_var.set("")
        self.texto_salida.delete(1.0, tk.END)


# --------------------------
# EJECUCIÓN PRINCIPAL
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppPlaneta(root)
    root.mainloop()