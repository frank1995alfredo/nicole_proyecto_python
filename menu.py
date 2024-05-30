from models import PaqueteTuristico, Venta
from estadisticas import Estadisticas

#LA CLASE MENU LLAMA A TODAS LA FUNCIONES CREDAS PARA REALIZAR LAS TAREAS CRUD
class Menu:
    
    #EN EL METODO CONSTRUCTOR, LE ESTABLES POR DEFAULT EL data_manager, ESTO PARA ACCEDER A LA FUNCIONES DE data_manager.py
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Ingreso de Paquetes turísticos")
            print("2. Consulta de Datos de Paquetes turísticos")
            print("3. Modificación de Datos de Paquetes turísticos")
            print("4. Eliminación de Datos de Paquetes turísticos")
            print("5. Ordenamiento de Paquetes turísticos")
            print("6. Listado de Datos de Paquetes turísticos")
            print("7. Estadísticas de ventas")
            print("8. Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.ingreso_datos()
            elif opcion == '2':
                self.consulta_datos()
            elif opcion == '3':
                self.modificacion_datos()
            elif opcion == '4':
                self.eliminacion_datos()
            elif opcion == '5':
                self.ordenamiento()
            elif opcion == '6':
                self.listado_datos()
            elif opcion == '7':
                self.estadisticas()
            elif opcion == '8':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def ingreso_datos(self):
        print("Ingreso de datos:")
        tipo_dato = input("¿Desea ingresar un Paquete o una Venta? (paquete/venta): ").strip().lower() #strip() para borrar espacios
                                                                                                       #lower() para convertit a minusculas
        if tipo_dato == 'paquete':
            paquete = input("Ingrese nombre del paquete: ")
            destino = input("Ingrese destino: ")
            duracion = int(input("Ingrese duración (días): "))
            precio = float(input("Ingrese precio: "))
            disponibilidad = input("Ingrese disponibilidad: ")
            registro = PaqueteTuristico(paquete, destino, duracion, precio, disponibilidad)# LLAMO AL MODELO PaqueteTuristico que esta en models.py
            self.data_manager.agregar_paquete(registro) #POR MEDIO DEL data_manager LLAMO A LA FUNCION agregar_paquete()
            print("Paquete ingresado correctamente.")
        elif tipo_dato == 'venta':
            venta = input("Ingrese ID de la venta: ")
            paquete = input("Ingrese nombre del paquete vendido: ")
            if not self.data_manager.buscar_paquete(paquete): #SI NO EXISTE EL PAQUETE EN paquetes_turisticos.csv
                print("El paquete no existe")
                return
            cedula_cliente = input("Ingrese cédula del cliente: ")
            #VALIDO LA CEDULA
            if len(cedula_cliente) != 10:
                print("Error, número de cédula incompleto")
                return
            if self.data_manager.validar_cedula(cedula_cliente) == False:
                print("Número de cédula incorrecto")
                return
            cantidad = int(input("Ingrese cantidad: "))
            total = cantidad * self.data_manager.buscar_paquete(paquete).precio  # Cálculo automático del total
            registro = Venta(venta, paquete, cedula_cliente, cantidad, total)
            self.data_manager.agregar_venta(registro)
            print("Venta ingresada correctamente.")
        else:
            print("Tipo de dato no reconocido.")


    #PERMITE CONSULTAR LOS DATOS DE UN REGISTRO ESPECIFICO DE VENTAS O PAQUETES
    def consulta_datos(self):
        print("Consulta de datos:")
        tipo_dato = input("¿Desea consultar un Paquete o una Venta? (paquete/venta): ").strip().lower()
        if tipo_dato == 'paquete':
            paquete = input("Ingrese nombre del paquete a buscar: ")
            registro = self.data_manager.buscar_paquete(paquete)
            if registro:
                print(f"Paquete encontrado: {registro.to_dict()}") #CONVIERTO A UN DICCIONARIO LA DATA 
                                                                   #Y LA PRESENTA
            else:
                print("Paquete no encontrado.")
        elif tipo_dato == 'venta':
            venta = input("Ingrese ID de la venta a buscar: ")
            registro = self.data_manager.buscar_venta(venta)
            if registro:
                print(f"Venta encontrada: {registro.to_dict()}")
            else:
                print("Venta no encontrada.")
        else:
            print("Tipo de dato no reconocido.")

    def modificacion_datos(self):
        print("Modificación de datos:")
        tipo_dato = input("¿Desea modificar un Paquete o una Venta? (paquete/venta): ").strip().lower()
        if tipo_dato == 'paquete':
            paquete = input("Ingrese nombre del paquete a modificar: ")
            nuevos_datos = {}
            for campo in ['destino', 'duracion', 'precio', 'disponibilidad']:
                nuevo_valor = input(f"Ingrese nuevo {campo} (dejar en blanco para mantener actual): ")
                if nuevo_valor:
                    nuevos_datos[campo] = int(nuevo_valor) if campo in ['duracion', 'disponibilidad'] else float(nuevo_valor) if campo == 'precio' else nuevo_valor
            if self.data_manager.modificar_paquete(paquete, nuevos_datos):
                print("Paquete modificado correctamente.")
            else:
                print("Paquete no encontrado.")
        elif tipo_dato == 'venta':
            venta = input("Ingrese ID de la venta a modificar: ")
            nuevos_datos = {}
            for campo in ['paquete', 'cedula_cliente', 'cantidad', 'total']:
                nuevo_valor = input(f"Ingrese nuevo {campo} (dejar en blanco para mantener actual): ")
                if nuevo_valor:
                    nuevos_datos[campo] = int(nuevo_valor) if campo == 'cantidad' else float(nuevo_valor) if campo == 'total' else nuevo_valor
            if self.data_manager.modificar_venta(venta, nuevos_datos):
                print("Venta modificada correctamente.")
            else:
                print("Venta no encontrada.")
        else:
            print("Tipo de dato no reconocido.")

    def eliminacion_datos(self):
        print("Eliminación de datos:")
        tipo_dato = input("¿Desea eliminar un Paquete o una Venta? (paquete/venta): ").strip().lower()
        if tipo_dato == 'paquete':
            paquete = input("Ingrese nombre del paquete a eliminar: ")
            if self.data_manager.eliminar_paquete(paquete):
                print("Paquete eliminado correctamente.")
            else:
                print("Paquete no encontrado.")
        elif tipo_dato == 'venta':
            venta = input("Ingrese ID de la venta a eliminar: ")
            if self.data_manager.eliminar_venta(venta):
                print("Venta eliminada correctamente.")
            else:
                print("Venta no encontrada.")
        else:
            print("Tipo de dato no reconocido.")

    def ordenamiento(self):
        print("Ordenamiento de datos:")
        tipo_dato = input("¿Desea ordenar Paquetes o Ventas? (paquetes/ventas): ").strip().lower()
        if tipo_dato == 'paquetes':
            criterio = input("Ingrese criterio de ordenamiento (paquete, destino, duracion, precio, disponibilidad): ")
            orden = input("Ingrese orden (ascendente/descendente): ")
            ascendente = orden.lower() == 'ascendente' #lower() CONVIERTE EL TEXTO A MINUSCULA
            self.data_manager.ordenar_paquetes(criterio, ascendente) #LLAMO AL METODO ordena_paquetes
            print("Paquetes ordenados correctamente.")
        elif tipo_dato == 'ventas':
            criterio = input("Ingrese criterio de ordenamiento (venta, paquete, cedula_cliente, cantidad, total): ")
            orden = input("Ingrese orden (ascendente/descendente): ")
            ascendente = orden.lower() == 'ascendente'
            self.data_manager.ordenar_ventas(criterio, ascendente)
            print("Ventas ordenadas correctamente.")
        else:
            print("Tipo de dato no reconocido.")

    def listado_datos(self):
        print("Listado de datos:")
        tipo_dato = input("¿Desea listar Paquetes o Ventas? (paquetes/ventas): ").strip().lower()
        if tipo_dato == 'paquetes':
            registros = self.data_manager.listar_paquetes()
            for registro in registros:
                print(registro.to_dict())
        elif tipo_dato == 'ventas':
            registros = self.data_manager.listar_ventas()
            for registro in registros:
                print(registro.to_dict())
        else:
            print("Tipo de dato no reconocido.")

    def estadisticas(self):
        print("Estadísticas:")
        registros_paquetes = self.data_manager.listar_paquetes()
        registros_ventas = self.data_manager.listar_ventas()
        
        estadisticas_paquetes = Estadisticas.calcular_estadisticas_generales_paquetes(registros_paquetes)
        estadisticas_ventas = Estadisticas.calcular_estadisticas_generales_ventas(registros_ventas)
         
        print("Estadisticas con datos de paquetes.")
        print("Número de paquetes")
        print(f"{estadisticas_paquetes['numero_paquetes']}")
        
        print("Precio total de los paquetes.")
        print(f"{estadisticas_paquetes['precio_total']}")
        
        print("Precio promedio de los paquetes.")
        print(f"{estadisticas_paquetes['precio_promedio']}")

        print("Estadísticas con datos de las ventas")
        print("Número de ventas.")
        print(f"{estadisticas_ventas['numero_ventas']}")
        
        print("Total de ingresos.")
        print(f"{estadisticas_ventas['total_ingresos']}")
            
    
        