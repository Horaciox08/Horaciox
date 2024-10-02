estudiantes = []
Lista Notas = []
cant estudiantes = int(imput("Ingrese la cantidad de estudiantes: "))
for i in range(cant estudiantes)
    print("Estudiante {}".format(i+1)")
    for q in range(3):
        nota = int(input("Ingrese su nota {}: ".format(q+1)))
        notas.append(nota)
    estudiantes.append(notas)
    notas = []
print(estudiantes)
