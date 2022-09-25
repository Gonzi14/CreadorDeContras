import random
import string
from random import randrange


def GuardarLasContras(contra, titulo):
    with open("Contras.txt", "a") as archivo:
        archivo.write(titulo + ": " + str(contra) + "\n")
        archivo.close()
    return contra


def GenerarLasContras(contraParametros, contraCantidad, titulo):
    contraFinal = ""
    if contraParametros == 1:
        for i in range(contraCantidad):
            valor = randrange(10)
            contraFinal = contraFinal + f"{str(valor)}"
         
    elif contraParametros == 2:
        for i in range(contraCantidad):
            DOS = randrange(3)
            if DOS == 0:
                valor = randrange(10)
            elif DOS == 1:
                valor = random.choice(string.ascii_lowercase)
            elif DOS == 2:
                valor = random.choice(string.ascii_uppercase)
            contraFinal = contraFinal + str(valor)
    print(contraFinal)   
    GuardarLasContras(contraFinal, titulo)
contraParametros = int(input("Desea que la contraseña sea con numeros(1) o con numeros y letras(2)? "))
contraCantidad = int(input("Cual es la longitud que desea que tenga esta contraseña? "))
GenerarLasContras(contraParametros, contraCantidad, input("Cual sera el nombre de la contra? "))


