calificacionTareas = float(input("Ingrese la calificación de tareas: "))
calificacionExamenParcial = float(input("Ingrese la calificación del examen parcial: "))
calificacionExamenFinal = float(input("Ingrese la calificación del examen final: "))
Tareas = 0.3 * calificacionTareas
ExamenParcial = 0.3 * calificacionExamenParcial
ExamenFinal = 0.4 * calificacionExamenFinal
calificacionFinal = Tareas + ExamenParcial + ExamenFinal
print(f"La calificación final del estudiante es: {calificacionFinal:.2f}")
