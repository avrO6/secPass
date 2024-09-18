import random
import string
import argparse

# Códigos ANSI para colores
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARILLO = "\033[33m"
RESET = "\033[0m"



parser = argparse.ArgumentParser(description="Herramienta para crear contraseñas seguras")
parser.add_argument("-l", "--long", type=int, default=8, help="Longitud de la contraseña")

args = parser.parse_args()

#funcion para generar contraseñas seguras
def genPass():
    chars = string.ascii_letters + string.digits + string.punctuation
    passwd = "".join(random.choice(chars) for i in range(args.long))
    return passwd

if args.long < 8:
    print(" ")
    print(ROJO + "[-] La longitud de la contraseña debe de ser mayor a 8 caracteres" + RESET)
    print(" ")
else:
    print(" ")
    print(VERDE + "[+]" + RESET + " Tu contraseña es: " + AZUL + genPass() + RESET)
    print(" ")
    
