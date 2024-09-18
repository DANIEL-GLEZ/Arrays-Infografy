import numpy as np
import time

alumnos = np.random.randint(0, 101, size=(500, 6))

def buscar_calificacion(alumno_id, materia_id):
    if 0 <= alumno_id < 500 and 0 <= materia_id < 6:
        return alumnos[alumno_id, materia_id]
    else:
        return "ID de alumno o materia fuera de rango"

start_time = time.time()
calificacion = buscar_calificacion(321, 5)
end_time = time.time()

print(f"La calificación del alumno 321 en la materia 5 es: {calificacion}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

import numpy as np
import time

# Crear una matriz de 50,000 alumnos y 500 materias con valores aleatorios(ejemplo de prueba valores grandes)
alumnos = np.random.randint(0, 101, size=(500000, 5000))

def buscar_calificacion(alumno_id, materia_id):
    if 0 <= alumno_id < 50000 and 0 <= materia_id < 500:
        return alumnos[alumno_id, materia_id]
    else:
        return "ID de alumno o materia fuera de rango"

start_time = time.time()
calificacion = buscar_calificacion(32100, 112)
end_time = time.time()

print(f"La calificación del alumno 32,100 en la materia 112 es: {calificacion}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
