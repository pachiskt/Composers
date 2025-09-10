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
            print("No hay gastos registrados.")
        else:
            for gasto in self.gastos:
                print(gasto)

    def total_gastos(self):
        return sum(gasto.monto for gasto in self.gastos)

    def reporte_por_categoria(self):
        reporte = {}
        for gasto in self.gastos:
            reporte[gasto.categoria] = reporte.get(gasto.categoria, 0) + gasto.monto
        return reporte

    def verificar_presupuesto(self):
        total = self.total_gastos()
        if self.presupuesto > 0:
            if total > self.presupuesto:
                print("⚠️ Has superado tu presupuesto!")
            else:
                print(f"Aún tienes disponible: S/ {self.presupuesto - total:.2f}")
        else:
            print("No has establecido un presupuesto.")


def menu():
    gestor = GestorFinanzas()
    while True:
        print("\n--- Gestor de Finanzas Personales ---")
        print("1. Establecer presupuesto")
        print("2. Agregar gasto")
        print("3. Mostrar gastos")
        print("4. Ver total de gastos")
        print("5. Ver reporte por categoría")
        print("6. Verificar presupuesto")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            presupuesto = float(input("Ingrese su presupuesto mensual: "))
            gestor.presupuesto = presupuesto
            print("Presupuesto establecido.")
        elif opcion == "2":
            categoria = input("Ingrese la categoría del gasto (ej. comida, transporte): ")
            monto = float(input("Ingrese el monto: "))
            gestor.agregar_gasto(categoria, monto)
            print("Gasto agregado.")
        elif opcion == "3":
            gestor.mostrar_gastos()
        elif opcion == "4":
            print(f"Total de gastos: S/ {gestor.total_gastos():.2f}")
        elif opcion == "5":
            reporte = gestor.reporte_por_categoria()
            for categoria, monto in reporte.items():
                print(f"{categoria}: S/ {monto:.2f}")
        elif opcion == "6":
            gestor.verificar_presupuesto()
        elif opcion == "7":
            print("Saliendo del gestor. ¡Adiós!")
            break
        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar el menú interactivo
if __name__ == "__main__":
    menu()
