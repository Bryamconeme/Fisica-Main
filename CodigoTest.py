# Importando las librerías necesarias
from math import tan, cos
import numpy as np
import matplotlib.pyplot as plt

# Solicitando los datos al usuario
try:
    # Solicitando al usuario la velocidad inicial, ángulo, y las posiciones iniciales en los ejes x e y.
    vi = float(input("Introduce la velocidad inicial en m/s: "))
    angulo = float(input("Introduce el ángulo en grados: "))
    x = float(input("Introduce la posición horizontal inicial (Eje X): "))
    y = float(input("Introduce la posición vertical inicial (Eje Y): "))
except ValueError:
    # En caso de que el usuario introduzca un valor no numérico, se mostrará un mensaje de error y se terminará el programa.
    print("Por favor, introduce solo números.")
    exit()

# Conversión del ángulo a radianes para usar en cálculos trigonométricos.
angulo_rad = np.radians(angulo)

# Constante de gravedad
g = 9.81

# Cálculo de los parámetros de la trayectoria
# Se utilizan las ecuaciones de la física para calcular los parámetros del movimiento parabólico.
a = tan(angulo_rad)
b = g / (2 * vi ** 2 * cos(angulo_rad) ** 2)
ymax = (vi ** 2 * np.sin(angulo_rad) ** 2) / (2 * g)
xmax = (vi ** 2 * np.sin(2 * angulo_rad)) / g
tmax = (vi * np.sin(angulo_rad)) / g
tv = 2 * tmax
vho = vi * cos(angulo_rad)
vver = vi * np.sin(angulo_rad)

# Imprimiendo los resultados
# Se muestran los resultados en un formato legible, con una precisión de dos decimales.
print("\nUn proyectil es lanzado con una velocidad inicial (Vi) de {0:.2f} m/s a un ángulo de {1:.2f}°".format(vi, angulo))
print("La velocidad horizontal inicial (Vxi) es: {0:.2f} m/s".format(vho))
print("La velocidad vertical inicial (Vyi) es: {0:.2f} m/s".format(vver))
print("\nLos parámetros más relevantes de su trayectoria son:")
print("Altura máxima alcanzada por el proyectil (Ymax): {0:.2f} m".format(ymax))
print("Alcance máximo horizontal del proyectil (Xmax): {0:.2f} m".format(xmax))
print("El tiempo máximo que alcanza el proyectil para el ángulo x (TiMax): {0:.2f} s".format(tmax))
print("El tiempo de vuelo que alcanza el proyectil para el angulo x (TiV): {0:.2f} s".format(tv))

# Definiendo la ecuación de la trayectoria
# Esta función define la trayectoria del proyectil en función de la distancia horizontal.
def f(x):
   return a * x - b * x ** 2

# Creando la gráfica
# Se crea un array de puntos en el eje x, desde 0 hasta xmax.
x = np.linspace(0, xmax, 500)
# Se crea un gráfico con un tamaño específico.
plt.figure(figsize=(10, 5))
# Se definen los títulos del gráfico y los ejes.
plt.suptitle("Evento físico simulado: Tiro parabólico", fontsize=20, color="blue")
plt.xlabel("Eje X", fontsize=20, color="red")
plt.ylabel("Eje Y", fontsize=20, color="red")
# Se añade un texto con la velocidad inicial al gráfico.
plt.text((np.argmax(f(x))/2), np.max(f(x)) + 1, "vi = {0:.2f} m/s".format(vi), fontsize=10)
# Se activa la rejilla del gráfico.
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
# Se añade un texto con el ángulo al gráfico.
plt.text(3, 1, "{0:.2f}°".format(angulo), fontsize=10)
# Se traza la función de la trayectoria en el gráfico.
plt.plot(x, f(x), "red", linewidth = 1, label = "{0:.2f}°".format(angulo))
# Finalmente, se muestra el gráfico.
plt.show()
