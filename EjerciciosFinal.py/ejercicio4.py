nombreProducto = input("Ingrese el nombre del producto: ")
precioProducto = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
precioConDescuento = precioProducto * (1 - (descuento / 100))
print(f"El producto coprado es: {nombreProducto}, y el precio del producto con descuento es: {precioConDescuento:.2f}")