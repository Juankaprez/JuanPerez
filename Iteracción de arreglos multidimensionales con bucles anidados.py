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

# Función para calcular el promedio total por ciudad
def calcular_promedio_ciudades(matriz_temperaturas, ciudades):
    """
    Calcula el promedio total de temperatura por ciudad.

    Parámetros:
    - temperaturas (list): matriz 3D [ciudad][semana][día] con temperaturas.
    - ciudades (list): lista con los nombres de las ciudades.

    Retorna:
    - dict: diccionario con el nombre de la ciudad como clave y su promedio como valor.
    """
    promedios_por_ciudad = {}

    for i, ciudad in enumerate(ciudades):
        suma = 0
        cantidad_datos = 0
        for semana in matriz_temperaturas[i]:
            for temp in semana:
                suma += temp
                cantidad_datos += 1
        promedio = suma / cantidad_datos if cantidad_datos else 0
        promedios_por_ciudad[ciudad] = promedio

    return promedios_por_ciudad

# Calcular y mostrar el promedio total por ciudad
promedios = calcular_promedio_ciudades(matriz_temperaturas, ciudades)

print("Promedio total de temperaturas por ciudad:\n")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")    
