import Funciones_conversiones:

def menu():
    print("***Menu***")
    print("Escoje que tipo de combersion quieres hacer:")
    print("1 : De metros a kilometros")
    print("2 : De kilometros a metros")
    print("3 : De gramos a kilogramos")
    print("4 : De Kilogramos a gramos")
    print("5 : De Celsius a Fahrenheit")
    print("6 : De Fahrenheit a Celsius")
    print("7 : Salir")

while True:
    menu()
    
    opcion = int(input("Escoje una opncion: "))

    if opcion == 7:
        print("Saliendo de la calculadora.")
        break
    #Pedir el numero para convertir a lo deseado
    dat1 = float(input("Ingrese el dato que quiere convertir"))
    # Llamar a la funcion correspondiente segun la opcion elegida
    if opcion == 1:
        print(f"Resultado: {conversion.kilometros(dat1)}")
    elif opcion == 2:
        print(f"Resultado: {conversion.metros(dat1)}")
    elif opcion == 3:
        print(f"Resultado: {conversion.kilogramos(dat1)}")
    elif opcion == 4:
        print(f"Resultado: {conversion.gramos(dat1)}")
    elif opcion == 5:
        print(f"Resultado: {conversion.celsius(dat1)}")
    elif opcion == 6:
        print(f"Resultado: {conversion.fahrenheit(dat1)}")
    else:
        print("Opcion no valida. Intentente nuevamente")
