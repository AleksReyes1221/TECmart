print("================================")
print("  CALCULADORA DE CALIFICACIONES")
print("================================")

nombre = input("Ingresa tu nombre: ")

calificacion1 = float(input("Ingresa la primera calificacion: "))
calificacion2 = float(input("Ingresa la segunda calificacion: "))
calificacion3 = float(input("Ingresa la tercera calificacion: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print("\n========= RESULTADOS =========")
print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 70:
    print("Resultado: APROBADO")
else:
    print("Resultado: REPROBADO")

print("==============================")