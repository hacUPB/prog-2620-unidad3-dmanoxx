### becas


promedio= float(input("Ingresa tu promedio: "))
nivel_econ= float(input("Ingresa tu nivel socioeconmico: "))

if promedio >= 9.0 or (nivel_econ == 1 and promedio >= 8.0):
    print("Felicidades, has obtenido una beca del 100%")
else:
    print("Lo siento, no has calificado para una beca")
