total_cuenta = float(input("Ingrese el total de la cuenta: "))
propina = total_cuenta * 0.10
total_con_propina = total_cuenta + propina
print(f"El total de la cuenta es: {total_cuenta:.2f}")
print(f"La propina es: {propina:.2f}")
print(f"El total de la cuenta con propina es: {total_con_propina:.2f}")