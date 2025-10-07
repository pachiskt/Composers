class TipoCombustible:
    def __init__(self, id_tipo_combustible, tipo_combustible):
        self._id_tipo_combustible = id_tipo_combustible
        self._tipo_combustible = tipo_combustible

    # Métodos Get
    def get_id_tipo_combustible(self):
        return self._id_tipo_combustible

    def get_tipo_combustible(self):
        return self._tipo_combustible

    # Métodos Set
    def set_id_tipo_combustible(self, id_tipo_combustible):
        self._id_tipo_combustible = id_tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def __str__(self):
        return self._tipo_combustible


class TipoAutomovil:
    def __init__(self, id_tipo_automovil, tipo_automovil):
        self._id_tipo_automovil = id_tipo_automovil
        self._tipo_automovil = tipo_automovil

    # Métodos Get
    def get_id_tipo_automovil(self):
        return self._id_tipo_automovil

    def get_tipo_automovil(self):
        return self._tipo_automovil

    # Métodos Set
    def set_id_tipo_automovil(self, id_tipo_automovil):
        self._id_tipo_automovil = id_tipo_automovil

    def set_tipo_automovil(self, tipo_automovil):
        self._tipo_automovil = tipo_automovil

    def __str__(self):
        return self._tipo_automovil

# --- Clase Principal ---
class Automovil:
    # 1. Constructor con todos los atributos
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color, velocidad_actual):
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = velocidad_actual

    # 2. Métodos Get y Set para cada atributo
    # Getters
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_motor(self):
        return self._motor

    def get_tipo_combustible(self):
        return self._tipo_combustible

    def get_tipo_automovil(self):
        return self._tipo_automovil

    def get_numero_puertas(self):
        return self._numero_puertas

    def get_cantidad_asientos(self):
        return self._cantidad_asientos

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def get_color(self):
        return self._color

    def get_velocidad_actual(self):
        return self._velocidad_actual

    # Setters
    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_motor(self, motor):
        self._motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self._tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas):
        self._numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos):
        self._cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self._color = color

    def set_velocidad_actual(self, velocidad_actual):
        self._velocidad_actual = velocidad_actual

    # 3. Método para calcular el tiempo estimado de llegada
    def calcular_tiempo_llegada(self, distancia_km):
        """Calcula el tiempo estimado en horas para recorrer una distancia."""
        if self._velocidad_actual == 0:
            return float('inf') # Retorna infinito si el auto está detenido
        tiempo_horas = distancia_km / self._velocidad_actual
        return tiempo_horas

    # 4. Método para mostrar los atributos
    def mostrar_atributos(self):
        """Imprime todos los atributos del automóvil en la consola."""
        print("\n--- Ficha del Automóvil ---")
        print(f"Marca: {self._marca}")
        print(f"Modelo (año): {self._modelo}")
        print(f"Motor (cilindraje en L): {self._motor}")
        print(f"Tipo de Combustible: {self._tipo_combustible}")
        print(f"Tipo de Automóvil: {self._tipo_automovil}")
        print(f"Número de Puertas: {self._numero_puertas}")
        print(f"Cantidad de Asientos: {self._cantidad_asientos}")
        print(f"Velocidad Máxima: {self._velocidad_maxima} km/h")
        print(f"Color: {self._color}")
        print(f"Velocidad Actual: {self._velocidad_actual} km/h")
        print("---------------------------\n")


# --- Ejecución Principal ---
print("--- Registro de un Nuevo Automóvil ---")
print("Por favor, ingrese los datos solicitados.")

# Ingreso de datos por consola
marca = input("Marca: ")
modelo = int(input("Modelo (año): "))
motor = float(input("Motor (cilindraje en litros): "))

# Selección de Tipo de Combustible
print("Seleccione el tipo de combustible: 1=Gasolina, 2=Diésel, 3=Gas Natural")
id_comb = int(input("Opción: "))
combustibles = {1: "Gasolina", 2: "Diésel", 3: "Gas Natural"}
tipo_comb = TipoCombustible(id_comb, combustibles.get(id_comb, "Desconocido"))

# Selección de Tipo de Automóvil
print("Seleccione el tipo de automóvil: 1=Ciudad, 2=Compacto, 3=Familiar, 4=SUV")
id_auto = int(input("Opción: "))
tipos_auto = {1: "Carro de ciudad", 2: "Compacto", 3: "Familiar", 4: "SUV"}
tipo_auto = TipoAutomovil(id_auto, tipos_auto.get(id_auto, "Desconocido"))

puertas = int(input("Número de puertas: "))
asientos = int(input("Cantidad de asientos: "))
vel_max = int(input("Velocidad máxima (km/h): "))

# Selección de Color
print("Seleccione el color: 1=Blanco, 2=Negro, 3=Rojo, 4=Azul")
id_color = int(input("Opción: "))
colores = {1: "Blanco", 2: "Negro", 3: "Rojo", 4: "Azul"}
color_auto = colores.get(id_color, "No especificado")

vel_act = int(input("Velocidad actual (km/h): "))

# 1. Crear un automóvil con los datos ingresados
mi_auto = Automovil(
    marca, modelo, motor, tipo_comb, tipo_auto,
    puertas, asientos, vel_max, color_auto, vel_act
)

# 2. Mostrar los valores del automóvil
print("\n>>> Automóvil creado exitosamente. Mostrando datos iniciales...")
mi_auto.mostrar_atributos()

# 3. Colocar su velocidad actual en 100 km/h
print(">>> Actualizando velocidad actual a 100 km/h...")
mi_auto.set_velocidad_actual(100)
print(f"Nueva velocidad actual: {mi_auto.get_velocidad_actual()} km/h")

# 4. Mostrar el tiempo estimado de llegada
distancia = float(input("\nIngrese la distancia a recorrer en kilómetros para calcular el tiempo de llegada: "))
tiempo = mi_auto.calcular_tiempo_llegada(distancia)

if tiempo == float('inf'):
    print("El automóvil está detenido, no se puede calcular el tiempo de llegada.")
else:
    print(f">>> El tiempo estimado de llegada para recorrer {distancia} km es de {tiempo:.2f} horas.")
