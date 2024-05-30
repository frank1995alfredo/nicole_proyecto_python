import math
import utilidades
from models import PaqueteTuristico, Venta

#LA CLASE DATA MANAGER, SEPARA LAS FUNCIONES QUE SE USARÁN EN menu.py,
#ESTO CON EL OBJETIVO DE QUE SE TENGA EL PROYECTO MAS ORDENADO
class DataManager:
    #SE CREA EL MÉTODO CONSTRUCTOR PARA INICIALIZAR LAS VARIABLES
    #file_path_paquetes, file_path_ventas son las rutas de los cvs
    def __init__(self, file_path_paquetes, file_path_ventas):
        self.file_path_paquetes = file_path_paquetes
        self.file_path_ventas = file_path_ventas
        self.paquetes = self.cargar_datos_paquetes()
        self.ventas = self.cargar_datos_ventas() 

    def cargar_datos_paquetes(self):
        registros = utilidades.leer_csv(self.file_path_paquetes)
        return [PaqueteTuristico(**registro) for registro in registros]

    def cargar_datos_ventas(self):
        registros = utilidades.leer_csv(self.file_path_ventas)
        return [Venta(**registro) for registro in registros]

    def guardar_datos_paquetes(self):
        #to_dict, convierte la data en un diccionario y con el for recorro la data
        registros = [registro.to_dict() for registro in self.paquetes]
        utilidades.escribir_csv(self.file_path_paquetes, registros)

    def guardar_datos_ventas(self):
        registros = [registro.to_dict() for registro in self.ventas]
        utilidades.escribir_csv(self.file_path_ventas, registros)

    def agregar_paquete(self, paquete):
        #.append sirve para agregrar los datos dentro de paquetes
        self.paquetes.append(paquete)
        self.guardar_datos_paquetes() #llama al metodo guardar_datos_paquetes

    def agregar_venta(self, venta):
        self.ventas.append(venta)
        self.guardar_datos_ventas()

    def buscar_paquete(self, paquete):
        for registro in self.paquetes:
            if registro.paquete == paquete:
                return registro
        return None

    def buscar_venta(self, venta):
        for registro in self.ventas:
            if registro.venta == venta:
                return registro
        return None

    def modificar_paquete(self, paquete, nuevos_datos):
        registro = self.buscar_paquete(paquete)
        if registro:
            for key, value in nuevos_datos.items():
                setattr(registro, key, value)
            self.guardar_datos_paquetes()
            return True
        return False

    def modificar_venta(self, venta, nuevos_datos):
        registro = self.buscar_venta(venta)
        if registro:
            for key, value in nuevos_datos.items():
                setattr(registro, key, value)
            self.guardar_datos_ventas()
            return True
        return False

    def eliminar_paquete(self, paquete):
        registro = self.buscar_paquete(paquete)
        if registro:
            self.paquetes.remove(registro)
            self.guardar_datos_paquetes()
            return True
        return False

    def eliminar_venta(self, venta):
        registro = self.buscar_venta(venta)
        if registro:
            self.ventas.remove(registro)
            self.guardar_datos_ventas()
            return True
        return False

    def listar_paquetes(self):
        return self.paquetes

    def listar_ventas(self):
        return self.ventas
  
    #LOS PAQUETES Y LAS VENTAS SE ORDENAN DEPENDIENDO DEL CRITERIO(descendente/ascendente)
    def ordenar_paquetes(self, criterio, ascendente=True):
        self.paquetes.sort(key=lambda registro: getattr(registro, criterio), reverse=not ascendente)
        self.guardar_datos_paquetes()

    def ordenar_ventas(self, criterio, ascendente=True):
        self.ventas.sort(key=lambda registro: getattr(registro, criterio), reverse=not ascendente)
        self.guardar_datos_ventas()

    #VALIDAR EL NÚMERO DE CÉDULA
    def validar_cedula(self, cedula):
        if len(cedula) != 10:
            raise Exception("Error: número de cédula incompleto")
        else:
            multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            
            # Convertir el map a una lista y luego tomar los primeros 9 elementos
            ced_array = list(map(int, list(cedula)))[0:9]
            ultimo_digito = int(cedula[9])
            
            resultado = []
            arr = zip(ced_array, multiplicador)  # Usar zip para iterar sobre ambos arreglos simultáneamente

            for (i, j) in arr:
                producto = i * j
                if producto < 10:
                    resultado.append(producto)
                else:
                    resultado.append(producto - 9)

            suma_resultado = sum(resultado)
            verificador_calculado = int(math.ceil(float(suma_resultado) / 10) * 10) - suma_resultado

            return ultimo_digito == verificador_calculado