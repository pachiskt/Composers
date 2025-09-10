from clases import Transaccion, Billetera

def mostrar_menu():
    """Imprime el menú de opciones en la consola."""
    print("\n--- Gestor de Finanzas Personales ---")
    print("1. Agregar nueva transacción")
    print("2. Mostrar todas las transacciones")
    print("3. Salir")
    print("-----------------------------------")

# Al iniciar el programa, creamos la billetera.
# El constructor de Billetera ahora se encarga de cargar los datos existentes.
mi_billetera = Billetera()

while True:
    mostrar_menu()
    opcion = input("Por favor, elige una opción: ")

    if opcion == '1':
        print("\n--- Agregar Nueva Transacción ---")
        try:
            monto = float(input("Ingresa el monto: S/"))
        except ValueError:
            print("Error: El monto debe ser un número. Intenta de nuevo.")
            continue

        categoria = input("Ingresa la categoría (ej: Comida, Transporte): ")
        fecha = input("Ingresa la fecha (ej: 2025-09-09): ")
        descripcion = input("Ingresa una descripción corta: ")

        nueva_transaccion = Transaccion(
            monto=monto, 
            categoria=categoria, 
            fecha=fecha, 
            descripcion=descripcion
        )
        
        # El método agregar_transaccion ahora también se encarga de guardar.
        mi_billetera.agregar_transaccion(nueva_transaccion)

    elif opcion == '2':
        mi_billetera.mostrar_transacciones()

    elif opcion == '3':
        print("¡Gracias por usar el gestor! Adiós.")
        break

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")