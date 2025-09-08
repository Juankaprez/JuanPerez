import random

# Definiciones básicas
ciudades = ["Bogotá", "Quito", "Buenos Aires", "New York"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear matriz 3D: ciudades x días x semanas
# matriz_temperaturas[ciudad][día][semana] = temperatura
matriz_temperaturas = []

for nombre_ciudad in ciudades:
    ciudad_datos = []
    for dia in dias_semana:
        semana_datos = []
        for semana in range(num_semanas):
            # Generamos una temperatura aleatoria entre 10 y 35 grados
            temp = round(random.uniform(10, 35), 1)
            semana_datos.append(temp)
        ciudad_datos.append(semana_datos)
    matriz_temperaturas.append(ciudad_datos)

# Mostrar promedios
print("\n📊 Promedio de temperaturas por ciudad y semana:\n")

for i_ciudad, nombre_ciudad in enumerate(ciudades):
    print(f"🌆 {nombre_ciudad}:")
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += matriz_temperaturas[i_ciudad][dia][semana]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    suma_estudiante = 0
    for nota in estudiante_notas:
        suma_estudiante += nota
    promedio_estudiante = suma_estudiante / len(estudiante_notas)
    print(f"El promedio del Estudiante {i+1} es: {promedio_estudiante:.2f}")
