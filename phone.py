import phonenumbers
import argparse
import requests
from phonenumbers import carrier, geocoder, timezone

#COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

parse = argparse.ArgumentParser("Ingrese un numero de telefono con el codigo del pais. Por Ejemplo: -N +571111111111")
parse.add_argument('-N', '--number', help="Numero de telefono")
parse = parse.parse_args()

#INICIA LA EJECUCION DE LA BUSQUEDA
try:
    if parse.number:
        banner = "| ====== ===LOCALIZADOR NUMERO DE TELEFONO ========= |"
        banner2 = " ------------ DEVELOPED BY DANIEL DAZA -----------"
        print(GREEN + banner + RESET)
        print(GREEN + banner2 + RESET)
        print()

        parse.number = phonenumbers.parse(parse.number)
        hora = timezone.time_zones_for_number(parse.number)
        operadora = carrier.name_for_number(parse.number, "es")
        pais = geocoder.description_for_number(parse.number, "es")
        n_valido = phonenumbers.is_valid_number(parse.number)
        n_existe = phonenumbers.is_possible_number(parse.number)
        tipo_numero = phonenumbers.number_type(parse.number)

        print(CYAN + "Zona Horaria Del Numero: " + RESET, hora[0])
        print(CYAN + "Operador: " + RESET, operadora)
        print(CYAN + "Pais: " + RESET, pais)

        #VALIDACIONES
        if tipo_numero == phonenumbers.PhoneNumberType.MOBILE:
            print(CYAN + "El número es móvil: " + RESET + "SI") 
        elif tipo_numero == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(CYAN + "El número es fijo: " + RESET + "SI")       
        else:
            print(CYAN + "[!] El número no es móvil ni fijo" + RESET)

        if n_valido:
            print(CYAN + "El numero es valido: " + RESET, "SI")
        else:
            print(CYAN + "[!] El numero es valido: " + RESET, "NO")

        if n_existe:
            print(CYAN + "Posibilidad que el numero exista: " + RESET, "SI")
        else:
            print(CYAN + "Posibilidad que el numero exista: " + RESET, "NO")
    else:
        print(CYAN + "\nUsage: python3 phone.py -N <Numero de telefono mas codigo del país>\nEjemplo: python3 phone.py -N +571111111111")
        print(RED + "[!] No se ha ingresado un numero de telefono valido")
except Exception as e:
    print(RED + "[!] La cadena proporcionada no es de un numero de telefono.")
