precio_compra = float(input("Introduce el precio de compra del artículo: "))
ganancia = 0.30

precio_venta = precio_compra + (precio_compra * ganancia)
print(f"El precio de venta del artículo es: {precio_venta:.0f}")