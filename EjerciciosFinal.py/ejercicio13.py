tiempo_lunes = float(input("Introduce el tiempo en minutos que tarda en recorrer la ruta del lunes: "))
tiempo_miercoles = float(input("Introduce el tiempo en minutos que tarda en recorrer la ruta del miercoles: "))
tiempo_viernes = float(input("Introduce el tiempo en minutos que tarda en recorrer la ruta del viernes: "))

tiempoPromedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3

print(f"El tiempo promedio de la ruta es: {tiempoPromedio:.0f} minutos")
