precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))

subtotal = precio1 + precio2 + precio3
iva = subtotal * 0.15
total = subtotal + iva
print (f"El subtotal es: {subtotal:.2f}")
print (f"El IVA es: {iva:.2f}")
print (f"El total es: {total:.2f}")