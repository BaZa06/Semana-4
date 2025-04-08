variable1 = int (input("Ingrese un número: "))
variable2 = int (input("Ingrese otro número: "))

print(f"El número {variable1} esta en la primera posición")
print(f"El número {variable2} esta en la segunda posición")

temporal = variable1
variable1 = variable2
variable2 = temporal

print (f"El número {variable1} esta en la primera posición")
print (f"El número {variable2} esta en la segunda posición")