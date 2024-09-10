import random
import string

# Códigos ANSI para colores
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARILLO = "\033[33m"
RESET = "\033[0m"



long = int(input('Indica la longitud de la contraseña(minimo 8): '))
chars = string.ascii_letters + string.digits + string.punctuation
passwd = "".join(random.choice(chars) for i in range(long))

if long < 8:
    print(" ")
    print(ROJO + "[-] La longitud de la contraseña debe de ser mayor a 8 caracteres" + RESET)
    print(" ")
else:
    print(" ")
    print(VERDE + "[+]" + RESET + " Tu contraseña es: " + AZUL + passwd + RESET)
    print(" ")