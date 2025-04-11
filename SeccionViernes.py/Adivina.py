#adivina un número
import random
numeroSecreto = random.randint(1, 10)
while True:
    print("Adivina el número entre 1 y 10")
    numeroUsuario = int(input("¿Cuál es tu número? "))
    if numeroUsuario == numeroSecreto:
        print("¡Felicidades!, adivinaste el número")
        break
    else:
        print("Intenta nuevamente")
        break
if(numeroSecreto == numeroUsuario):
    print("¡Felicidades!, te ganaste 10 puntos extras")
else:
    print("Lo siento, tenesque invitar a un churro a todos los compañeros.")
    if(numeroUsuario > numeroSecreto):
        print("El número es menor")
    else:
        print("El número es mayor")