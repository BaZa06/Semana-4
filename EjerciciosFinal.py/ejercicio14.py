presupuesto_anual_hospital = int(input("Ingrese el presupuesto anual para el hospital: "))

pediatría = 0.42
urgencias = 0.37
traumatología = 0.21

presupuesto_pediatría = presupuesto_anual_hospital * pediatría
presupuesto_urgencias = presupuesto_anual_hospital * urgencias
presupuesto_traumatología = presupuesto_anual_hospital* traumatología
print(f"El presupuesto para el área de urgencias es {presupuesto_urgencias:.2f}")
print(f"El presupuesto para el área de pediatría es {presupuesto_pediatría:.2f}")
print(f"El presupuesto para el área de traumatología es {presupuesto_traumatología:.2f}")