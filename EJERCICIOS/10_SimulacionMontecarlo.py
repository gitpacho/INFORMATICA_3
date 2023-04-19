import numpy
from collections import defaultdict
from matplotlib import pyplot
import itertools

#length es la longitud de nuestro sistema.
#J es la constante de intercambio.
#kB es la constante de Boltzmann.

length = 5
J = 1.0
kB = 1.0

#Contenedores
sites = []               # contenedor de posiciones
spins = dict()           # contenedor de espines
nbhs = defaultdict(list) # contenedor de vecinos

#  Creación de la muestra
for x, y in itertools.product(range(length), range(length)):
    sites.append((x,y))

#Creación del estado inicial aleatorio

def random_configuration():
    for site in sites:
        spins[site] = numpy.random.choice([-1, 1])

random_configuration()
#print(spins)


#Impresión de imagen
def plot_spins():
    pyplot.figure()
    colors = {1: "red", -1: "blue"}
    for site, spin in spins.items():
        x, y = site
        pyplot.quiver(x, y, 0, spin, pivot="middle", color=colors[spin])
    pyplot.xticks(range(0,length))
    pyplot.yticks(range(0,length))
    pyplot.gca().set_aspect("equal")
    #pyplot.grid()
    pyplot.savefig("EJERCICIOS/estadoInicial.png")
    pyplot.close()
plot_spins()



#Asignación de primeros vecinos
nbhs = defaultdict(list)
for site in spins.keys():
    x, y = site
    if x + 1 < length:  #vecino derecha
        nbhs[site].append(((x + 1) % length, y))
    if x - 1 >= 0:      #vecino izquierda
        nbhs[site].append(((x - 1) % length, y))
    if y + 1 < length:  #vecino arriba
        nbhs[site].append((x, (y + 1) % length))
    if y - 1 >= 0:      #Vecino abajo
        nbhs[site].append((x, (y - 1) % length))

print(nbhs)


#Creación de funciones para cálculo de 
# energía local, 
# energía total 
# y magnetización

def energy_site(site):
    energy = 0.0
    for nbh in nbhs[site]:
        energy += spins[site] * spins[nbh]
    return -J * energy

def total_energy():
    energy = 0.0
    for site in sites:
        energy += energy_site(site)
    return 0.5 * energy

def magnetization():
    mag = 0.0
    for spin in spins.values():
        mag += spin
    return mag

print("magnetization = ", magnetization())

#====================================================
#== metodología metropolis para el sistema Ising-2D=>


def metropolis(site, T):
    #oldSpin = spins[site]
    oldEnergy = energy_site(site)
    spins[site] *= -1    # Se hace el cambio anticipadamente.
                         # Luego verificamos en 
                         # las condiciones if-else
                         # si es valido o no
    newEnergy = energy_site(site)
    deltaE = newEnergy - oldEnergy
    if deltaE <= 0:
        pass     #Se acepta el cambio
    else:
        if numpy.random.uniform(0, 1) <= numpy.exp(-deltaE/(kB*T)):
            pass #Se acepta el cambio
        else:
            spins[site] *= -1  #Se rechaza el cambio

def monte_carlo_step(T):
    for i in range(len(sites)):
        int_rand_site = numpy.random.randint(0, len(sites))
        rand_site = sites[int_rand_site]
        metropolis(rand_site, T)


#==========SIMULACION======================>

amount_mcs = 100  #Pasos montecarlo
T_high = 5.0
T_low = 0.01
step = -0.1

#Ciclo de temperatura
temps = numpy.arange(T_high, T_low, step)
energies = numpy.zeros(shape=(len(temps), amount_mcs))
magnetizations = numpy.zeros(shape=(len(temps), amount_mcs))
random_configuration()
for ind_T, T in enumerate(temps):
    for i in range(amount_mcs):
        monte_carlo_step(T)
        energies[ind_T, i] = total_energy()
        magnetizations[ind_T, i] = magnetization()

# Revisar la simulacion 
# Dibujar el sistema final
# Graficar la energía y la magnetizacion en funcion de 
# la temperatura


plot_spins()
tau = amount_mcs // 2
energy_mean = numpy.mean(energies[:, tau:], axis=1)
magnetization_mean = abs(numpy.mean(magnetizations[:, tau:], axis=1))

pyplot.figure(figsize=(12,3))
pyplot.subplot(1,2,1)
pyplot.plot(temps, energy_mean, label="Energy")
pyplot.legend()
pyplot.xlabel(r"$T$")
pyplot.ylabel(r"$\left<E\right>$")
pyplot.grid()

pyplot.subplot(1,2,2)
pyplot.plot(temps, magnetization_mean, label="Magnetization")
pyplot.legend()
pyplot.xlabel(r"$T$")
pyplot.ylabel(r"$\left<M\right>$")
pyplot.grid()
pyplot.savefig("EJERCICIOS/simulacion.png")











