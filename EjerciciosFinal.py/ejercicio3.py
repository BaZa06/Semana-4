salario_empleado = int(input("Introduce el salario del empleado: "))
incremento = 0.08
nuevo_salario = salario_empleado * (1 + incremento)
servicios_nuevo_salario = nuevo_salario * 0.025
total_recibido = nuevo_salario - servicios_nuevo_salario
print(f"El salario del empleado con el incremento del 8% es: {nuevo_salario:.0f}")
print(f"El salario nuevo menos el descuento por los servicios: {servicios_nuevo_salario:.0f}")
print(f"El total recibido por el empleado es: {total_recibido:.0f}")