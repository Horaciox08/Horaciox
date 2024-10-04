import random

def adivina_el_numero():
    print("¡Bienvenido al juego de adivinar el número!")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        estimacion = int(input("Adivina un número entre 1 y 100: "))
        intentos += 1

        if estimacion < numero_secreto:
            print("Demasiado bajo. ¡Inténtalo de nuevo!")
        elif estimacion > numero_secreto:
            print("Demasiado alto. ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            adivinado = True

adivina_el_numero()
