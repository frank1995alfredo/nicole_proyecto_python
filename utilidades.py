import csv

#FUNCIONES PARA LEER LOS ARCHIVOS CSV Y ESCRIBIR 
#mode = 'r' indica que se leerá los datos del archivo
def leer_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

#mode = 'w' indica que se escribirá o insertará los datos en el archivo
def escribir_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys()) #escribe fila a fila en el documento
        writer.writeheader()
        writer.writerows(data)
