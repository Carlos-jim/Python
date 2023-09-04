import secrets
import string

letras = string.ascii_letters
digitos = string.digits
caracter_especial = string.punctuation

alfabeto = letras + digitos + caracter_especial

longitud = int(input("Ingrese la cantidad de dígitos que desea: "))

passw = []
for i in range(longitud):
    passw.append(secrets.choice(alfabeto))

passw = ''.join(passw)
print(passw)
