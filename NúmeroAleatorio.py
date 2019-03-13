import random
intentos = 0
print("¡Hola!")
numero = random.randrange(1,11)
print("Estoy pensando en un numero entre 1 y 10")

while intentos < 3:
    print("Intenta adivinar")
    res = input()
    res = int(res)

    intentos = intentos + 1

    if res < numero:
        print("Uy, es un numero muy pequeño")
    if res > numero:
        print("Uy, es un numero muy grande")
    if res == numero:
        break

if res == numero:
    intentos = str(intentos)
    print("Buen trabajo, has adivinado mi numero en " + intentos + " intentos.")

if res != numero:
    numero = str(numero)
    print("Ese no es el numero que estaba pensando, era: " + numero)