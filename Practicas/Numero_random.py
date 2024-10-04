import random
print("!Bienvenido al juego Adivina el Numero!")
print("Estoy pensando en un numero entre 1 y 100. Puedes adivinar cual es?")
num_secret = random.randint(1,5)
while True:
    try:
        num = int(input("Ingrese el número: "))
        if num < num_secret:
            print("El número es alt0. Intenta nuevamente.")
        elif num > num_secret:
            print("El número es bajo. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Adivinaste el número {num_secret}.")
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

