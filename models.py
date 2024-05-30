
class PaqueteTuristico:
    #CREO EL METODO CONSTRUCTOR E INICIALIZO LAS VARIABLES
    def __init__(self, paquete, destino, duracion, precio, disponibilidad):
        self.paquete = paquete
        self.destino = destino
        self.duracion = int(duracion)
        self.precio = float(precio)
        self.disponibilidad = disponibilidad

    #FUNCION PARA RETORNAR LA DATA EN UN DICCIONARIO
    def to_dict(self):
        return {
            'paquete': self.paquete,
            'destino': self.destino,
            'duracion': self.duracion,
            'precio': self.precio,
            'disponibilidad': self.disponibilidad
        }

class Venta:
    def __init__(self, venta, paquete, cedula_cliente, cantidad, total):
        self.venta = venta
        self.paquete = paquete
        self.cedula_cliente = cedula_cliente
        self.cantidad = cantidad
        self.total = total

    def to_dict(self):
        return {
            'venta': self.venta,
            'paquete': self.paquete,
            'cedula_cliente': self.cedula_cliente,
            'cantidad': self.cantidad,
            'total': self.total
        }
