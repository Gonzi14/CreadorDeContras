import random
import string
from random import randrange
def GuardarLasContras(contra, titulo):
    with open("GeneradorDeContras\Contras.txt", "a") as archivo:
        archivo.write(titulo + ": " + str(contra) + ".\n")
        archivo.close()
    return contra
def GenerarLasContras(contraParametros, contraCantidad, titulo):
    contraFinal = ""
    if contraParametros == 1:
        valor = randrange(10)
        contraFinal =+ f"{valor}"
        print(valor)
        print(contraFinal)    
    elif contraParametros == 2:
        for i in range(1, contraCantidad):
            DOS = randrange(1)
            if DOS == 1:
                valor = randrange(10)
            else:
                valor = random.choice(string.ascii_lowercase)
            contraFinal =+ f"{string(int(valor))}"
            print(valor)
            print(contraFinal)   

    return GuardarLasContras(contraFinal, titulo)
    #contraParametros = int(input("Desea que la contraseña sea con numeros(1), con numeros y letras(2) o numeros,"
    #                             "letras y "
     #                        "mayusculas(3)?"))
    #contraCantidad = int(input("Cual es la longitud que desea que tenga esta contraseña?"))
    #GenerarLasContras(contraParametros, contraCantidad)
GenerarLasContras(2, 10, "prueba")

