class Estadisticas:
    #FINCIONES PARA CALCULAR ESTADÍSTICAS BÁSICAS
    @staticmethod #EL @staticmethod es un decorador de python que
                  #indica que las funciones podrán ser llamadas desde la clase
                  #sin crear el objeto
    def calcular_estadisticas_generales_paquetes(paquetes):
        numero_paquetes = len(paquetes) #len(paquetes) dará el número total de paquetes
        precio_total = sum(float(paquete.precio) for paquete in paquetes) #suma los precios de cada paquete
        precio_promedio = precio_total / numero_paquetes if numero_paquetes > 0 else 0 #calcula el precio promedio
        
        #retona la data en un diccionario para que puedan se accedidos uno por uno
        return {
            "numero_paquetes": numero_paquetes,
            "precio_total": precio_total,
            "precio_promedio": precio_promedio
        }
    
    @staticmethod
    def calcular_estadisticas_generales_ventas(ventas):
        numero_ventas = len(ventas)
        total_ingresos = sum(float(venta.total) for venta in ventas)
        
        return {
            "numero_ventas": numero_ventas,
            "total_ingresos": total_ingresos
        }