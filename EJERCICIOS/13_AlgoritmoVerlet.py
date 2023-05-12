import numpy as np
import matplotlib.pyplot as plt

#Constantes

G = 1 # Cte gravitacional
m = 1 # Masa de la tierra

# FUNCIONES
def aceleracion(x, y, eje):
    if eje == 'x':
        return - G * m * x / (x**2 + y**2)**1.5
    elif eje == 'y':
        return - G * m * y / (x**2 + y**2)**1.5

print("a_x =>",aceleracion(1, 0, "x"))
print("a_y =>",aceleracion(0, 1, "y"))

def paso_euler(r_0, v_0, a_0, delta_t):
    return r_0 + v_0 * delta_t +  (a_0 * delta_t**2) / 2

def paso_verlet(r_1, r_0, a_1, delta_t):
    return 2 * r_1 - r_0 + (a_1 * delta_t**2)


# PARAMETROS DE CONTROL

delta_t = 0.01
pasos = 700

# CONDICIONES INICIALES

x_0, y_0 = 0, 1
vx_0, vy_0 = 1.1, 0
ax_0, ay_0 = aceleracion(x_0, y_0, 'x'), aceleracion(x_0, y_0, 'y')

# PASO EULER

x_1 = paso_euler(x_0, vx_0, ax_0, delta_t)
y_1 = paso_euler(y_0, vy_0, ay_0, delta_t)
ax_1 = aceleracion(x_1, y_1, 'x')
ay_1 = aceleracion(x_1, y_1, 'y')

# PASOS VERLET
x_lista = [x_0, x_1]
y_lista = [y_0, y_1]
t_lista = [0, delta_t]


def paso_verlet(r_1, r_0, a_1, delta_t):
    return 2 * r_1 - r_0 + (a_1 * delta_t**2)

for i in range(pasos): 
    x_2 = paso_verlet(x_1, x_0, ax_1, delta_t)
    y_2 = paso_verlet(y_1, y_0, ay_1, delta_t)
    x_lista.append(x_2)
    y_lista.append(y_2)
    
    # ACTUALIZACION
    ax_1 = aceleracion(x_2, y_2, 'x')
    ay_1 = aceleracion(x_2, y_2, 'y')  
    x_0, x_1 = x_1, x_2
    y_0, y_1 = y_1, y_2

    radio = 0.05
    if (x_2**2 + y_2**2)**0.5 < radio:
      print("Ha caido a la tierra")
      break

plt.figure(figsize=(3,3))
plt.scatter(0,0, s = 300, c="g")
plt.plot(x_lista,y_lista, "--k")
plt.show()