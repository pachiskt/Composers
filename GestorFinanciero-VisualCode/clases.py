import json

class Transaccion:
    """
    Representa una única transacción financiera (gasto o ingreso).
    """
    def __init__(self, monto, categoria, fecha, descripcion):
        self.monto = monto
        self.categoria = categoria
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        """
        Devuelve una representación en texto de la transacción.
        """
        monto_formateado = f"{self.monto:.2f}"
        return f"[{self.fecha}] {self.categoria}: S/{monto_formateado} ({self.descripcion})"

    def a_diccionario(self):
        """
        Convierte el objeto Transaccion a un diccionario para poder guardarlo en JSON.
        """
        return {
            "monto": self.monto,
            "categoria": self.categoria,
            "fecha": self.fecha,
            "descripcion": self.descripcion
        }

class Billetera:
    """
    Representa una billetera que gestiona una colección de transacciones.
    """
    def __init__(self, archivo="datos.json"):
        self.archivo = archivo
        self.transacciones = []
        self.cargar_transacciones()

    def agregar_transaccion(self, transaccion):
        """
        Agrega una nueva transacción a la lista y guarda los cambios.
        """
        self.transacciones.append(transaccion)
        self.guardar_transacciones()
        print("--> Transacción agregada con éxito.")

    def mostrar_transacciones(self):
        """
        Muestra todas las transacciones registradas en la billetera.
        """
        if not self.transacciones:
            print("No hay transacciones registradas todavía.")
            return

        print("\n--- Resumen de Transacciones ---")
        for transaccion in self.transacciones:
            print(transaccion)
        print("------------------------------")

    def guardar_transacciones(self):
        """
        Guarda la lista de transacciones en un archivo JSON.
        """
        # Convertimos cada objeto Transaccion a un diccionario
        lista_de_diccionarios = [t.a_diccionario() for t in self.transacciones]
        with open(self.archivo, 'w') as f:
            json.dump(lista_de_diccionarios, f, indent=4)

    def cargar_transacciones(self):
        """
        Carga las transacciones desde un archivo JSON al iniciar el programa.
        """
        try:
            with open(self.archivo, 'r') as f:
                lista_de_diccionarios = json.load(f)
                # Convertimos cada diccionario de vuelta a un objeto Transaccion
                self.transacciones = [Transaccion(**datos) for datos in lista_de_diccionarios]
        except FileNotFoundError:
            # Si el archivo no existe, simplemente empezamos con una lista vacía.
            self.transacciones = []
        except json.JSONDecodeError:
            # Si el archivo está vacío o corrupto, también empezamos de cero.
            self.transacciones = []