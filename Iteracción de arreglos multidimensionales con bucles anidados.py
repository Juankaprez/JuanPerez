# Ejemplo de un arreglo multidimensional (matriz) de notas
# Cada fila es un estudiante, cada columna es una nota
notas_estudiantes = [
    [85, 92, 78],  # Estudiante 1
    [90, 88, 95],  # Estudiante 2
    [70, 75, 80]   # Estudiante 3
]

# Variables para calcular el promedio
total_sum = 0
total_notas = 0

# Bucle exterior: recorre los estudiantes (filas)
for estudiante_notas in notas_estudiantes:
    # Bucle interior: recorre las notas de cada estudiante (columnas)
    for nota in estudiante_notas:
        total_sum += nota       # Sumar la nota al total general
        total_notas += 1      # Incrementar el contador de notas

# Calcular el promedio general de todas las notas
promedio_general = total_sum / total_notas

print(f"El promedio general de todas las notas es: {promedio_general:.2f}")

# --- Opcional: Calcular el promedio por estudiante ---

print("\n--- Promedios por estudiante ---")
for i, estudiante_notas in enumerate(notas_estudiantes):
    suma_estudiante = 0
    for nota in estudiante_notas:
        suma_estudiante += nota
    promedio_estudiante = suma_estudiante / len(estudiante_notas)
    print(f"El promedio del Estudiante {i+1} es: {promedio_estudiante:.2f}")
