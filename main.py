from data_manager import DataManager
from menu import Menu

if __name__ == "__main__":
    data_manager = DataManager('D:/ORODELTI_POWER_BI/PROYECTO_FINCAS2/carga_datos/proyecto/paquetes_turisticos.csv',
                               'D:/ORODELTI_POWER_BI/PROYECTO_FINCAS2/carga_datos/proyecto/ventas.csv')
    menu = Menu(data_manager)
    menu.mostrar_menu()
