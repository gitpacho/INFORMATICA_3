#=============== EJERCICIOS CICLO WHILE===================

#==> EJERCICIO 1
"""Realice un programa que lea una secuencia de números, y cuente cuántos números son pares y cuántos son impares. 
El programa termina cuando se ingresa el número cero."""

#==> Ejercicio 2 
"""Utilizando el ciclo while, imprima las siguientes secuencias de numeros:
=> 2,4,5,8,10,11,14,16,17,20 ...598, 599
=> 2,4,8,16,32,64,128, .. 1048576
=> 1,1,2,3,5,8, ... 2178309"""


#=============== EJERCICIOS CICLO FOR===================

#==> EJERCICIO 1
""" Realice los siguientes programas:
      a) Programa que calcule los primeros 100 terminos de la serie de fibonacci
      b) Programa que determine todos los divisores de un numero n
      c) Programa que determine si un número n es primo
      d) Programa que sume los digitos de un numero cualquiera. Ejemplo: numero=> 8791, rta=> 25 
      e) Programa que sume los digitos pares de un numero cualquiera """

#==> EJERCICIO 2 
""" El rendimiento de los empleados de una empresa es el siguiente:
--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A"       "C"   
Donde "A" es alto, "B" aceptable  y "C"  insuficiente. 
Determine ¿cuales empleados pueden solicitar un aumento salarial y cuáles pueden ser despedidos? """


empleados = ["Emplea_1",  "Emplea_2",  "Emplea_3",  "Emplea_4",  "Emplea_5",  "Emplea_6",  "Emplea_7",  "Emplea_8",  "Emplea_9",  "Emplea_10",  "Emplea_11",  "Emplea_12",  "Emplea_13",  "Emplea_14",  "Emplea_15",  "Emplea_16",  "Emplea_17",  "Emplea_18",  "Emplea_19",  "Emplea_20",  "Emplea_21",  "Emplea_22",  "Emplea_23",  "Emplea_24",  "Emplea_25",  "Emplea_26",  "Emplea_27"]
rendimiento =  ["C" ,"B","B",  "B",  "C","B","A",  "C", "B",  "A",  "C", "B",  "B",  "B",   "B",  "A", "B",  "A",   "A",  "C", "B",  "B",  "B",   "B",   "C", "A", "C" ]

indices = range(0, len(empleados))

posibleAumentoSalarial = []
posibleDespedido = []

for indice in indices:
      if rendimiento[indice] == "A":
            empleado = empleados[indice]
            posibleAumentoSalarial.append(empleado)
      elif rendimiento[indice] == "C":
            empleado = empleados[indice]
            posibleDespedido.append(empleado)
  
print("Aumento salarial: ", posibleAumentoSalarial)
print("Despidos: ", posibleDespedido)


  #==> EJERCICIO 3 
""" El rendimiento deportivo de un grupo de atletas es el siguiente:
-------------- Deportista_1  Deportista_2  Deportista_3  Deportista_4  Deportista_5  Deportista_6  Deportista_7  Deportista_8  Deportista_9  Deportista_10  Deportista_11  Deportista_12  Deportista_13  Deportista_14  Deportista_15  Deportista_16  Deportista_17  Deportista_18  Deportista_19  Deportista_20  Deportista_21  Deportista_22  Deportista_23  Deportista_24  Deportista_25  Deportista_26  Deportista_27 
Rendimiento --    "A"           "B"           "C"            "B"            "B"           "B"          "C"           "B"             "A"           "C"          "B"          "A"             "C"             "B"          "B"              "B"           "B"             "A"           "B"            "A"           "A"             "C"             "B"             "B"          "B"            "B"            "C"             
Edad ---------     42            60            18             20             35            25           60            30              19            42           21           17              39              30           28               34            27              23            23             20            25             "40"             31             32            45             26             17             
Donde "A" es alto, "B" aceptable  y "C"  insuficiente. Determine:
  => ¿Cuántos atletas tienen un rendimiento alto, aceptable e insuficiente?
  => ¿Cuántos atletas mayores de 40 años, tienen rendimiento alto?
  => ¿Cuantos atletas menores de 25, tienen un rendimiento insuficiente?
  => ¿Cuales deportistas entre 30 y 40 años tienen rendimiento aceptable?
  => ¿Cuales deportistas menores de 30 tienen rendimiento alto
  => ¿Cuales deportistas mayores de 35 tienen rendimiento insuficiente?
(Intente utilizar un solo ciclo para resolver las preguntas) """