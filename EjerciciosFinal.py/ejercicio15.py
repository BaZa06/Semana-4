nombre = input("Introduce el nombre del trabajador: ")
horasTrabajadas = float(input("Introduce las horas trabajadas: "))
precio_fijo_horaa = float(input("Introduce el precio fijo por hora: "))
descuentoRenta = 0.05
sueldoBruto = horasTrabajadas * precio_fijo_horaa
sueldoDescuento = sueldoBruto * descuentoRenta
sueldoNeto = sueldoBruto - sueldoDescuento

print(f"El nombre del trabajador es: {nombre}")
print(f"El sueldo bruto es de: {sueldoBruto:.2f}")
print(f"El descuento de renta es de: {sueldoDescuento:.2f}")
print(f"El sueldo neto es de: {sueldoNeto:.2f}")