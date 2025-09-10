import datetime
import json
from typing import List, Dict, Any, Optional

# CLASE PARA GESTIONAR LAS CATEGORÍAS DE GASTOS
class GestorCategorias:
    def __init__(self):
        self.categorias = self.cargar_categorias_predeterminadas()
    
    def cargar_categorias_predeterminadas(self) -> List[Dict[str, Any]]:
        """Carga categorías predeterminadas con sus palabras clave"""
        categorias_predeterminadas = [
            {"id": 1, "nombre": "Alimentación", "palabras_clave": "comida,restaurante,mercado,supermercado,desayuno,almuerzo,cena"},
            {"id": 2, "nombre": "Transporte", "palabras_clave": "pasaje,taxi,uber,combustible,transporte,bus"},
            {"id": 3, "nombre": "Educación", "palabras_clave": "libros,utiles,curso,universidad,colegio,matricula"},
            {"id": 4, "nombre": "Entretenimiento", "palabras_clave": "cine,película,netflix,spotify,juegos,diversión"},
            {"id": 5, "nombre": "Salud", "palabras_clave": "medicina,doctor,hospital,farmacia,seguro"},
            {"id": 6, "nombre": "Servicios", "palabras_clave": "luz,agua,internet,teléfono,alquiler"},
            {"id": 7, "nombre": "Ropa", "palabras_clave": "ropa,zapatos,accesorios,tienda"},
            {"id": 8, "nombre": "Otros", "palabras_clave": ""}
        ]
        return categorias_predeterminadas
    
    def clasificar_gasto(self, descripcion: str) -> str:
        """Clasifica automáticamente un gasto basado en su descripción"""
        descripcion_lower = descripcion.lower()
        
        for categoria in self.categorias:
            if categoria["palabras_clave"]:
                palabras = categoria["palabras_clave"].split(",")
                for palabra in palabras:
                    if palabra.strip() and palabra.strip() in descripcion_lower:
                        return categoria["nombre"]
        
        return "Otros"
    
    def obtener_todas_categorias(self) -> List[Dict[str, Any]]:
        """Obtiene todas las categorías disponibles"""
        return self.categorias
    
    def obtener_nombres_categorias(self) -> List[str]:
        """Obtiene solo los nombres de las categorías"""
        return [categoria["nombre"] for categoria in self.categorias]
    
    def agregar_categoria_manual(self, nombre_categoria: str):
        """Agrega una categoría manualmente si no existe"""
        nombres_existentes = self.obtener_nombres_categorias()
        if nombre_categoria not in nombres_existentes:
            nuevo_id = max([c["id"] for c in self.categorias]) + 1 if self.categorias else 1
            self.categorias.append({
                "id": nuevo_id,
                "nombre": nombre_categoria,
                "palabras_clave": ""
            })

# CLASE PARA GESTIONAR LOS GASTOS
class GestorGastos:
    def __init__(self, gestor_categorias: GestorCategorias):
        self.gestor_categorias = gestor_categorias
        self.gastos: List[Dict[str, Any]] = []
        self.ultimo_id = 0
    
    def registrar_gasto(self, monto: float, descripcion: str, categoria_manual: Optional[str] = None, fecha: Optional[str] = None, metodo_pago: str = "Efectivo") -> str:
        """Registra un nuevo gasto en el sistema"""
        if categoria_manual:
            categoria = categoria_manual
            # Agregar la categoría manual si no existe
            self.gestor_categorias.agregar_categoria_manual(categoria)
        else:
            categoria = self.gestor_categorias.clasificar_gasto(descripcion)
        
        if fecha is None:
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.ultimo_id += 1
        nuevo_gasto = {
            "id": self.ultimo_id,
            "monto": monto,
            "descripcion": descripcion,
            "categoria": categoria,
            "fecha": fecha,
            "metodo_pago": metodo_pago
        }
        
        self.gastos.append(nuevo_gasto)
        return categoria
    
    def obtener_gastos(self, dias: Optional[int] = None) -> List[Dict[str, Any]]:
        """Obtiene todos los gastos, opcionalmente filtrados por días"""
        if not self.gastos:
            return []
        
        if dias:
            fecha_limite = (datetime.datetime.now() - datetime.timedelta(days=dias)).strftime("%Y-%m-%d")
            gastos_filtrados = [
                gasto for gasto in self.gastos 
                if gasto["fecha"] >= fecha_limite
            ]
            return sorted(gastos_filtrados, key=lambda x: x["fecha"], reverse=True)
        else:
            return sorted(self.gastos, key=lambda x: x["fecha"], reverse=True)
    
    def obtener_resumen_por_categoria(self, dias: Optional[int] = None) -> Dict[str, float]:
        """Obtiene un resumen de gastos por categoría"""
        gastos = self.obtener_gastos(dias)
        resumen = {}
        
        for gasto in gastos:
            categoria = gasto["categoria"]
            if categoria in resumen:
                resumen[categoria] += gasto["monto"]
            else:
                resumen[categoria] = gasto["monto"]
        
        return resumen
    
    def generar_reporte_mensual(self, mes: Optional[int] = None, año: Optional[int] = None) -> Dict[str, Any]:
        """Genera un reporte mensual de gastos"""
        if mes is None:
            mes = datetime.datetime.now().month
        if año is None:
            año = datetime.datetime.now().year
        
        primer_dia = datetime.date(año, mes, 1)
        if mes == 12:
            ultimo_dia = datetime.date(año + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            ultimo_dia = datetime.date(año, mes + 1, 1) - datetime.timedelta(days=1)
        
        gastos_mes = [
            gasto for gasto in self.gastos
            if primer_dia.strftime("%Y-%m-%d") <= gasto["fecha"][:10] <= ultimo_dia.strftime("%Y-%m-%d")
        ]
        
        total = sum(gasto["monto"] for gasto in gastos_mes)
        resumen_categoria = {}
        
        for gasto in gastos_mes:
            categoria = gasto["categoria"]
            if categoria in resumen_categoria:
                resumen_categoria[categoria] += gasto["monto"]
            else:
                resumen_categoria[categoria] = gasto["monto"]
        
        return {
            "mes": mes,
            "año": año,
            "total_gastos": total,
            "gastos": gastos_mes,
            "resumen_categoria": resumen_categoria
        }

# CLASE PARA GESTIONAR LOS OBJETIVOS DE AHORRO
class GestorAhorros:
    def __init__(self):
        self.objetivos: List[Dict[str, Any]] = []
        self.ultimo_id = 0
    
    def establecer_objetivo_ahorro(self, nombre: str, monto_objetivo: float, fecha_limite: Optional[str] = None, descripcion: str = ""):
        """Establece un nuevo objetivo de ahorro"""
        self.ultimo_id += 1
        nuevo_objetivo = {
            "id": self.ultimo_id,
            "nombre": nombre,
            "monto_objetivo": monto_objetivo,
            "monto_actual": 0.0,
            "fecha_limite": fecha_limite,
            "descripcion": descripcion
        }
        
        self.objetivos.append(nuevo_objetivo)
    
    def actualizar_objetivo_ahorro(self, objetivo_id: int, monto_agregado: float):
        """Actualiza el monto actual de un objetivo de ahorro"""
        for objetivo in self.objetivos:
            if objetivo["id"] == objetivo_id:
                objetivo["monto_actual"] += monto_agregado
                break
    
    def obtener_objetivos_ahorro(self) -> List[Dict[str, Any]]:
        """Obtiene todos los objetivos de ahorro"""
        return self.objetivos

# CLASE PARA LA EXPORTACIÓN DE DATOS
class ExportadorDatos:
    def __init__(self, gestor_gastos: GestorGastos, gestor_ahorros: GestorAhorros):
        self.gestor_gastos = gestor_gastos
        self.gestor_ahorros = gestor_ahorros
    
    def exportar_datos(self, formato: str = "json") -> str:
        """Exporta todos los datos a formato JSON o CSV"""
        gastos = self.gestor_gastos.obtener_gastos()
        objetivos = self.gestor_ahorros.obtener_objetivos_ahorro()
        
        datos = {
            "gastos": gastos,
            "objetivos_ahorro": objetivos
        }
        
        if formato.lower() == "json":
            return json.dumps(datos, indent=2, ensure_ascii=False)
        else:
            csv_data = "Tipo,ID,Monto,Descripcion,Categoria,Fecha,MetodoPago\n"
            for gasto in gastos:
                csv_data += f"Gasto,{gasto['id']},{gasto['monto']},\"{gasto['descripcion']}\",{gasto['categoria']},{gasto['fecha']},{gasto['metodo_pago']}\n"
            
            for objetivo in objetivos:
                csv_data += f"Objetivo,{objetivo['id']},{objetivo['monto_objetivo']},\"{objetivo['descripcion']}\",,,{objetivo['fecha_limite']}\n"
            
            return csv_data

# CLASE PRINCIPAL DEL SISTEMA
class SistemaFinanzasEstudiantes:
    def __init__(self):
        self.gestor_categorias = GestorCategorias()
        self.gestor_gastos = GestorGastos(self.gestor_categorias)
        self.gestor_ahorros = GestorAhorros()
        self.exportador = ExportadorDatos(self.gestor_gastos, self.gestor_ahorros)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        while True:
            print("\n" + "=" * 50)
            print("SISTEMA DE GESTIÓN DE FINANZAS PARA ESTUDIANTES")
            print("=" * 50)
            print("1. Registrar nuevo gasto")
            print("2. Ver gastos recientes")
            print("3. Ver resumen por categoría")
            print("4. Generar reporte mensual")
            print("5. Gestionar objetivos de ahorro")
            print("6. Exportar datos")
            print("7. Salir")
            print("=" * 50)
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_gasto()
            elif opcion == "2":
                self.ver_gastos_recientes()
            elif opcion == "3":
                self.ver_resumen_categorias()
            elif opcion == "4":
                self.generar_reporte_mensual()
            elif opcion == "5":
                self.gestionar_objetivos_ahorro()
            elif opcion == "6":
                self.exportar_datos()
            elif opcion == "7":
                print("¡Gracias por usar el Sistema de Gestión de Finanzas para Estudiantes!")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
    
    def registrar_gasto(self):
        """Registra un nuevo gasto en el sistema"""
        print("\n--- REGISTRAR NUEVO GASTO ---")
        
        while True:
            try:
                monto = float(input("Ingrese el monto del gasto: S/. "))
                if monto <= 0:
                    print("El monto debe ser mayor a cero. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
        
        descripcion = input("Ingrese la descripción del gasto: ")
        
        # Preguntar si desea ingresar categoría manualmente
        opcion_categoria = input("¿Desea ingresar manualmente la categoría? (s/n): ").strip().lower()
        categoria_manual = None
        if opcion_categoria == 's':
            categoria_manual = input("Ingrese la categoría manualmente: ").strip()
        
        while True:
            metodo_pago = input("Ingrese el método de pago (Efectivo, Tarjeta, Yape, Plin, etc.): ").strip()
            if metodo_pago:
                break
            print("El método de pago no puede estar vacío.")
        
        categoria = self.gestor_gastos.registrar_gasto(monto, descripcion, categoria_manual, None, metodo_pago)
        print(f"¡Gasto registrado exitosamente! Categoría: {categoria}")
    
    def ver_gastos_recientes(self):
        """Muestra los gastos recientes"""
        print("\n--- GASTOS RECIENTES ---")
        
        while True:
            try:
                dias_input = input("¿De cuántos días atrás desea ver los gastos? (Enter para todos): ")
                if not dias_input:
                    dias = None
                    break
                dias = int(dias_input)
                if dias <= 0:
                    print("El número de días debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        gastos = self.gestor_gastos.obtener_gastos(dias)
        
        if not gastos:
            print("No se encontraron gastos en el período seleccionado.")
            return
        
        print(f"\n{'Fecha':<20} {'Descripción':<30} {'Monto':<10} {'Categoría':<15} {'Método Pago':<10}")
        print("-" * 85)
        
        for gasto in gastos:
            fecha = gasto['fecha'][:10]  # Mostrar solo la fecha, no la hora
            descripcion = gasto['descripcion'][:28] + "..." if len(gasto['descripcion']) > 30 else gasto['descripcion']
            print(f"{fecha:<20} {descripcion:<30} S/. {gasto['monto']:<7.2f} {gasto['categoria']:<15} {gasto['metodo_pago']:<10}")
        
        total = sum(gasto['monto'] for gasto in gastos)
        print("-" * 85)
        print(f"{'TOTAL':<51} S/. {total:.2f}")
    
    def ver_resumen_categorias(self):
        """Muestra el resumen de gastos por categoría"""
        print("\n--- RESUMEN DE GASTOS POR CATEGORÍA ---")
        
        while True:
            try:
                dias_input = input("¿De cuántos días atrás desea ver el resumen? (Enter para todos): ")
                if not dias_input:
                    dias = None
                    break
                dias = int(dias_input)
                if dias <= 0:
                    print("El número de días debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        resumen = self.gestor_gastos.obtener_resumen_por_categoria(dias)
        
        if not resumen:
            print("No se encontraron gastos en el período seleccionado.")
            return
        
        total = sum(resumen.values())
        
        print(f"\n{'Categoría':<20} {'Monto':<10} {'Porcentaje':<12}")
        print("-" * 42)
        
        for categoria, monto in sorted(resumen.items(), key=lambda x: x[1], reverse=True):
            porcentaje = (monto / total) * 100 if total > 0 else 0
            print(f"{categoria:<20} S/. {monto:<7.2f} {porcentaje:.1f}%")
        
        print("-" * 42)
        print(f"{'TOTAL':<20} S/. {total:.2f} {'100.0%':<12}")
    
    def generar_reporte_mensual(self):
        """Genera un reporte mensual de gastos"""
        print("\n--- REPORTE MENSUAL ---")
        
        while True:
            try:
                mes_input = input("Ingrese el mes (1-12, Enter para mes actual): ")
                if not mes_input:
                    mes = datetime.datetime.now().month
                else:
                    mes = int(mes_input)
                
                if mes < 1 or mes > 12:
                    print("El mes debe estar entre 1 y 12.")
                    continue
                
                año_input = input("Ingrese el año (Enter para año actual): ")
                if not año_input:
                    año = datetime.datetime.now().year
                else:
                    año = int(año_input)
                
                break
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        
        reporte = self.gestor_gastos.generar_reporte_mensual(mes, año)
        
        nombre_mes = datetime.date(1900, mes, 1).strftime('%B')
        print(f"\nREPORTE MENSUAL - {nombre_mes.upper()} {año}")
        print("=" * 50)
        print(f"Total gastado: S/. {reporte['total_gastos']:.2f}")
        print(f"Cantidad de gastos: {len(reporte['gastos'])}")
        
        if reporte['gastos']:
            print("\nResumen por categoría:")
            print("-" * 30)
            
            for categoria, monto in reporte['resumen_categoria'].items():
                porcentaje = (monto / reporte['total_gastos']) * 100 if reporte['total_gastos'] > 0 else 0
                print(f"{categoria:<15} S/. {monto:<7.2f} ({porcentaje:.1f}%)")
        else:
            print("\nNo hay gastos registrados para este mes.")
    
    def gestionar_objetivos_ahorro(self):
        """Gestiona los objetivos de ahorro"""
        print("\n--- GESTIÓN DE OBJETIVOS DE AHORRO ---")
        
        while True:
            print("\n1. Ver objetivos de ahorro")
            print("2. Crear nuevo objetivo")
            print("3. Actualizar objetivo existente")
            print("4. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.ver_objetivos_ahorro()
            elif opcion == "2":
                self.crear_objetivo_ahorro()
            elif opcion == "3":
                self.actualizar_objetivo_ahorro()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
    
    def ver_objetivos_ahorro(self):
        """Muestra los objetivos de ahorro"""
        objetivos = self.gestor_ahorros.obtener_objetivos_ahorro()
        
        if not objetivos:
            print("No hay objetivos de ahorro registrados.")
            return
        
        print(f"\n{'ID':<3} {'Nombre':<20} {'Objetivo':<10} {'Ahorrado':<10} {'Progreso':<15} {'Fecha Límite':<12}")
        print("-" * 70)
        
        for objetivo in objetivos:
            progreso = (objetivo['monto_actual'] / objetivo['monto_objetivo']) * 100 if objetivo['monto_objetivo'] > 0 else 0
            fecha = objetivo['fecha_limite'] if objetivo['fecha_limite'] else "Sin fecha"
            print(f"{objetivo['id']:<3} {objetivo['nombre']:<20} S/. {objetivo['monto_objetivo']:<8.2f} S/. {objetivo['monto_actual']:<8.2f} {progreso:.1f}%{'':<6} {fecha:<12}")
    
    def crear_objetivo_ahorro(self):
        """Crea un nuevo objetivo de ahorro"""
        print("\n--- CREAR NUEVO OBJETIVO DE AHORRO ---")
        
        nombre = input("Nombre del objetivo: ")
        
        while True:
            try:
                monto_objetivo = float(input("Monto objetivo: S/. "))
                if monto_objetivo <= 0:
                    print("El monto objetivo debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
        
        fecha_limite = input("Fecha límite (YYYY-MM-DD, o Enter para sin fecha): ")
        if not fecha_limite:
            fecha_limite = None
        
        descripcion = input("Descripción (opcional): ")
        
        self.gestor_ahorros.establecer_objetivo_ahorro(nombre, monto_objetivo, fecha_limite, descripcion)
        print("¡Objetivo de ahorro creado exitosamente!")
    
    def actualizar_objetivo_ahorro(self):
        """Actualiza un objetivo de ahorro existente"""
        objetivos = self.gestor_ahorros.obtener_objetivos_ahorro()
        
        if not objetivos:
            print("No hay objetivos de ahorro registrados para actualizar.")
            return
        
        self.ver_objetivos_ahorro()
        
        try:
            objetivo_id = int(input("\nIngrese el ID del objetivo a actualizar: "))
            monto_agregado = float(input("Monto a agregar: S/. "))
            
            # Verificar si el objetivo existe
            objetivo_existe = any(objetivo['id'] == objetivo_id for objetivo in objetivos)
            if not objetivo_existe:
                print("Error: No existe un objetivo con el ID proporcionado.")
                return
            
            self.gestor_ahorros.actualizar_objetivo_ahorro(objetivo_id, monto_agregado)
            print("¡Objetivo actualizado exitosamente!")
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos válidos.")
    
    def exportar_datos(self):
        """Exporta los datos a un archivo"""
        print("\n--- EXPORTAR DATOS ---")
        
        formato = input("Formato (JSON/CSV, Enter para JSON): ").strip().lower()
        if not formato or formato not in ["json", "csv"]:
            formato = "json"
        
        datos = self.exportador.exportar_datos(formato)
        
        # Guardar en archivo
        nombre_archivo = f"finanzas_exportacion_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.{formato}"
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(datos)
        
        print(f"Datos exportados exitosamente al archivo: {nombre_archivo}")
        
        # Mostrar preview
        if formato == "json":
            preview = datos[:500] + "..." if len(datos) > 500 else datos
            print(f"\nVista previa:\n{preview}")

# FUNCIÓN PRINCIPAL
def main():
    """Función principal del programa"""
    sistema = SistemaFinanzasEstudiantes()
    
    print("=" * 60)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE FINANZAS PARA ESTUDIANTES")
    print("=" * 60)
    print("Nota: Los datos no se guardarán entre sesiones.")
    print("Cada vez que inicie el programa, comenzará con datos vacíos.")
    print("=" * 60)
    
    sistema.mostrar_menu_principal()

if __name__ == "__main__":
    main()