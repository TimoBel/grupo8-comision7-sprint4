# En la descripción de los campos, falta el campo TIPO, que es un string que puede tener los siguientes valores  "EMITIDO" o "DEPOSITADO" \
# Dado un DNI, no pueden existir cheques con mismo numero de cheque
# Para exportar el CSV: Se exporta NumeroCuentaDestino, Valor, FechaOrigen y FechaPago


import csv
from encodings import normalize_encoding
import filecmp
from operator import le, truediv
import os.path

def entradaCorrecta(entrada):
    if (len(entrada) < 4) or (len(entrada) > 6):
        print("Entrada invalida")
        exit()

def handlerSalida(salida):
    if salida == "PANTALLA":
        modo = "r"
        chequearExistencia(nombre)
        procesarArchivo(modo)
        print(filtrarCheques(dni, tipo))
    elif salida == "CSV":
        # TODO: GENERAR CSV
        modo = "a"
        procesarArchivo(modo)
    else: 
        print("Tipo de salida no valida")
        exit()

def chequearExistencia(nombreArchivo):
    if not os.path.exists(nombreArchivo):
        print("El archivo no existe")
        exit()

def procesarArchivo(modo):
    with open("test.csv", "r") as file:
        fileCSV = csv.reader(file)
        header = next(fileCSV)
        for row in fileCSV:
            cheque = dict(zip(header, row))
            cheques.append(cheque)

# TODO: NO ME IMPRIME TIPO Y DNI
def filtrarCheques(dni, tipo):
    filtradoDni = list(filter(filtrarPorDni, cheques))

    if len(filtradoDni) == 0:
        print("DNI no encontrado")
        exit()
    
    chequearMismoNumeroCheque(filtradoDni)
    
    filtradoPorDniYTipo = list(filter(filtrarPorTipo, filtradoDni))
    if len(filtradoPorDniYTipo) == 0:
        print("Cheque de tipo {tipo} no encontrado para DNI {dni}")
        exit()

    return filtradoPorDniYTipo

    
# TODO: FALTA HACER ESTE CHEQUEO
def chequearMismoNumeroCheque(cheques):
    # filter(lambda cheque: cheque["NroCheque"] )
    return True

def filtrarPorDni(cheque):
    if (cheque["DNI"] == dni):
        return True
    return False

def filtrarPorTipo(cheque):
    if (cheque["Tipo"] == tipo):
        return True
    return False
 
# -------------------------------------------------------------------------------------

header = []
cheques = []

entrada = input("Nombre del archivo, DNI, Salida, Tipo, Estado (opcional), Rango(opcional): ")
entrada = entrada.split(",")

entradaCorrecta(entrada)

nombre = entrada[0].strip()
dni = entrada[1].strip()
salida = entrada[2].strip()
tipo = entrada[3].strip()

if len(entrada) == 5:
    estado = entrada[4].strip()

elif len(entrada) == 6: 
    estado = entrada[4].strip()
    rango = entrada[5]

handlerSalida(salida)
# test.csv, 11580999, PANTALLA, 123, 123











