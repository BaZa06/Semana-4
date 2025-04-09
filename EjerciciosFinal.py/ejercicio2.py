mujeres = int(input("Introduce el número de mujeres en el aula: "))
hombres = int(input("Introduce el número de hombres en el aula: "))
total_estudiantes = mujeres + hombres
promedio_hombres = hombres / total_estudiantes * 100 
promedio_mujeres = 100 - promedio_hombres
print(f"El total de estudiantes en el aula es: {total_estudiantes}")
print(f"El promedio de hombres en el aula es: {promedio_hombres:.2f} %")
print(f"El promedio de mujeres en el aula es: {promedio_mujeres:.2f} %")