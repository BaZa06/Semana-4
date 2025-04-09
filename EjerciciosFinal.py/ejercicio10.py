presion = float(input("Introduce la presión del objeto: "))
teperatura = float(input("Introduce la temperatura del objeto: "))
volummen = float(input("Introduce el volumen del objeto: "))

masa = presion * volummen / (0.37 * (teperatura + 460))

print(f"La masa del objeto es: {masa:.2f} kg")
