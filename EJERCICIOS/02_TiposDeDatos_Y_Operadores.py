''' 
1) Imprimir en la terminal
    dos enteros en una misma linea
    dos flotantes en una misma linea
    dos strings en una misma linea
    dos booleanos en una misma linea
    dos listas en una misma linea
    dos tuplas en una misma linea
    un diccionario en una misma linea
    un conjunto en una misma linea
'''

print(2,3)
print(2.1, 3.0)
print("asa", "hola")
print(True, True)
print([], [0])
print((0,),(0,1))
print({1:"uno", 2:"dos"})
print({"A", "B", "C", "D"})


"2) Resolver con los operadores que considere conveniente"

""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

P1 = (5,4,5) 
P2 = (0,10,9)

distancia = ((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 + (P1[2] - P2[2])**2) ** 0.5
print("distancia => ", distancia)


""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """


nota1 = 1 
nota2 = 2
nota3 = 2
nota4 = (3 - ((nota1*0.15)+(nota2*0.25)+(nota3*0.20))) / 0.4
print("nota necesaria => ", nota4)


""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """
a1 = 3
a2 = 5
# x1 = x1_0 + v1_0 * (t1 - t1_0) + a1/2 * (t1 - t1_0)**2  => x1 = 0 + 0 + a1/2 * (t - 0)**2
# x2 = x2_0 + v2_0 * (t2 - t2_0) + a2/2 * (t2 - t2_0)**2  => x2 = 0 + 0 + a2/2 * (t - 10)**2
# x1 = x2  => a1/2 * (t)**2 = a2/2 * (t - 10)**2  => a1/2 * (t**2) = a2/2 * (t**2 - 20*t + 100)
# a1/2 * (t**2) - a2/2 * (t**2) + 10*a2*t = 50*a2 => (a1 - a2) * (t**2) + 20*a2*t = 100*a2
# (a1/a2 - 1) * (t**2) + 20*t - 100 = 0
# t = (-20 +- (20**2 - 4*(a1/a2 - 1)*(-100))**0.5)/(2*(a1/a2 - 1))
t1 = (-20 + (20**2 - 4*((a1/a2) - 1)*(-100))**0.5)/(2*((a1/a2) - 1))
t2 = (-20 - (20**2 - 4*((a1/a2) - 1)*(-100))**0.5)/(2*((a1/a2) - 1))
print("solucion tiempo de rebase => ", t1, t2)


""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.
Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      
¿Cuanto debe pagar cada estudiante? """

JUAN = (True,True,False,True,False)
CAMILA = (True,True,False,False,False)
JOSE = (True,False,True,False,False)
MARIA = (True,True,True,False,False)

costos_individuales = [0,0,0,0]

for dia in range(5):
    if JUAN[dia] or CAMILA[dia] or JOSE[dia] or MARIA[dia]:
        personas_movilizadas = JUAN[dia] + CAMILA[dia] + JOSE[dia] + MARIA[dia]
        if JUAN[dia]:
            costos_individuales[0] += 15000/personas_movilizadas
        if CAMILA[dia]:
            costos_individuales[1] += 15000/personas_movilizadas
        if JOSE[dia]:
            costos_individuales[2] += 15000/personas_movilizadas
        if MARIA[dia]:
            costos_individuales[3] += 15000/personas_movilizadas
    else:
        print("else")
        for i in range(4):
            costos_individuales[i] += 2500

print(costos_individuales, sum(costos_individuales))


    
        









