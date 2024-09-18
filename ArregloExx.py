import numpy as np
import time

# Crear un arreglo de 500,000 alumnos y 7 materias con datos aleatorios
num_alumnos = 500000
num_materias = 7
arreglo = np.random.randint(0, 101, size=(num_alumnos, num_materias))

# Imprimir todos los valores del arreglo
print("Valores del arreglo:")
start_time = time.time()
for i in range(num_alumnos):
    for j in range(num_materias):
        print(f"Alumno {i + 1}, Materia {j + 1}: {arreglo[i, j]}")
end_time = time.time()

# Buscar al alumno 32,101 y la materia 6
alumno = 32100  # Índice 32,101 (0-based index)
materia = 5     # Índice 6 (0-based index)
nota = arreglo[alumno, materia]

# Mostrar el resultado de la búsqueda y el tiempo de ejecución
print(f"\nLa nota del alumno {alumno + 1} en la materia {materia + 1} es: {nota}")
print(f"Tiempo de ejecución para imprimir todos los valores: {end_time - start_time} segundos")
