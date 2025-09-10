import tkinter as tk
from tkinter import messagebox

class Gasto:
    def __init__(self, categoria, monto):
        self.categoria = categoria
        self.monto = monto

    def __str__(self):
        return f"{self.categoria}: S/ {self.monto:.2f}"


class GestorFinanzas:
    def __init__(self, presupuesto=0):
        self.gastos = []
        self.presupuesto = presupuesto

    def agregar_gasto(self, categoria, monto):
        gasto = Gasto(categoria, monto)
        self.gastos.append(gasto)

    def mostrar_gastos(self):
        if not self.gastos:
            return "No hay gastos registrados."
        return "\n".join(str(gasto) for gasto in self.gastos)

    def total_gastos(self):
        return sum(gasto.monto for gasto in self.gastos)

    def reporte_por_categoria(self):
        reporte = {}
        for gasto in self.gastos:
            reporte[gasto.categoria] = reporte.get(gasto.categoria, 0) + gasto.monto
        return "\n".join(f"{c}: S/ {m:.2f}" for c, m in reporte.items())

    def verificar_presupuesto(self):
        total = self.total_gastos()
        if self.presupuesto > 0:
            if total > self.presupuesto:
                return "⚠️ Has superado tu presupuesto!"
            else:
                return f"Aún tienes disponible: S/ {self.presupuesto - total:.2f}"
        else:
            return "No has establecido un presupuesto."


class App:
    def __init__(self, root):
        self.gestor = GestorFinanzas()
        self.root = root
        self.root.title("Gestor de Finanzas Personales")

        # Presupuesto
        tk.Label(root, text="Presupuesto (S/):").grid(row=0, column=0, sticky="w")
        self.presupuesto_entry = tk.Entry(root)
        self.presupuesto_entry.grid(row=0, column=1)
        tk.Button(root, text="Establecer", command=self.set_presupuesto).grid(row=0, column=2)

        # Agregar gasto
        tk.Label(root, text="Categoría:").grid(row=1, column=0, sticky="w")
        self.categoria_entry = tk.Entry(root)
        self.categoria_entry.grid(row=1, column=1)

        tk.Label(root, text="Monto (S/):").grid(row=2, column=0, sticky="w")
        self.monto_entry = tk.Entry(root)
        self.monto_entry.grid(row=2, column=1)

        tk.Button(root, text="Agregar gasto", command=self.add_gasto).grid(row=2, column=2)

        # Botones de reporte
        tk.Button(root, text="Mostrar gastos", command=self.show_gastos).grid(row=3, column=0)
        tk.Button(root, text="Total de gastos", command=self.show_total).grid(row=3, column=1)
        tk.Button(root, text="Reporte por categoría", command=self.show_reporte).grid(row=3, column=2)
        tk.Button(root, text="Verificar presupuesto", command=self.show_presupuesto).grid(row=4, column=1)

        # Área de resultados
        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.grid(row=5, column=0, columnspan=3)

    def set_presupuesto(self):
        try:
            self.gestor.presupuesto = float(self.presupuesto_entry.get())
            messagebox.showinfo("Presupuesto", "Presupuesto establecido correctamente")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido")

    def add_gasto(self):
        try:
            categoria = self.categoria_entry.get()
            monto = float(self.monto_entry.get())
            self.gestor.agregar_gasto(categoria, monto)
            messagebox.showinfo("Gasto", "Gasto agregado correctamente")
            self.categoria_entry.delete(0, tk.END)
            self.monto_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido")

    def show_gastos(self):
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, self.gestor.mostrar_gastos())

    def show_total(self):
        total = self.gestor.total_gastos()
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, f"Total de gastos: S/ {total:.2f}")

    def show_reporte(self):
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, self.gestor.reporte_por_categoria())

    def show_presupuesto(self):
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, self.gestor.verificar_presupuesto())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()