#Métodos de las cadenas
print("--------------cadenas---------------")
cadena = "hola mundo cruel"
print("directorio", dir(cadena))
print(cadena.upper())
print(cadena.lower())
print(cadena.center(50))
print(cadena.count("o"))
print(cadena[6])
print(cadena[5:10:1])

#====================== MÉTODOS DE STRINGS ====================

#==> EJERCICIO 1
"A continuación se encuentra el poema el salmon"

"""
TÍTULO: EL SALMÓN
PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR,MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
"""

"""a) Corrija el poema de tal manera que:
      Los indicadores de título y párrafo desaparezcan
      Corregir el uso de mayúsculas y minúsculas según las reglas gramaticales.
      El titulo esté en formato de título.
      Separar los cuatro versos de cada párrafo en renglones sucesivos
      Generar un espacio de renglon entre titulo-parrafo y párrafo-parrafo
      El título debe estar centrado.   
   b) Contar el número de veces que aparece cada vocal
      contar el numero de lineas del poema.
      Reemplazar las palabras: salmón ==> tiburón
                               tiburón ==> salmón
   c) Verificar si el contenido del poemas es: alfabetico
                                               alfanumerico
                                               decimal
                                               digitos
   d) Utilizar la indexación para extraer los elementos ubicados
      en los índices: 0, 10, 100, último índices
   e) Utilizar slicing para extraer los elementos ubicados en:
      - Indices pares.
      - Indices impares.
      - Cada quinto elemento, empezando desde el 20
      - Cada tercer elemento, pero empezando desde el indice 4 y terminando en el 62
      - Desde la mitad hacia adelante
      - Todos pero al revés
      - Cada segundo elemento, pero al revés"""

#Métodos de las listas
lista = [1,2,3,4]
#print(dir(lista))

#Metodos de las tuplas
tupla = (10,20,30)
#print(dir(tupla))

#Metodos de los diccionarios
diccionario = {1:"uno", 2:"dos", 3:"tres"}
#print(dir(diccionario))



#====================== EJERCICIOS MÉTODOS DE LISTAS ====================

#==> EJERCICIO 1

""" Realice las siguientes operaciones sobre listas:
        * ["A","B","C"] Elimine el último elemento de la lista
                        Luego agregue su nombre al final de la lista                  
        * [100,200,300] Elimine el segundo elemento de la lista,
                        Luego agregue su edad como segundo elemento de la lista
        * [1,2,3,4]     Elimine el último elemento de la lista
                        Luego agrege los valores 100, 200, 300 al final de la lista
                        Elimine el segundo elemento de la lista
                        Luego inserte el valor -1 en la segunda posición de la lista
        * Contruya una sola lista con los elementos resultantes de las 3 listas anteriores."""

lista = ["A","B","C"]
print("lista =>", lista)
lista.pop()
print("elemento borrado =>", lista)
lista.append("Cristian Pachon")
print("nuevo elemento =>", lista)

lista2 = [100,200,300]
print("lista2 =>", lista2)
lista2.pop(1)
print("lista2 actualizada =>", lista2)
lista2.insert(1, 40)
print("lista2 actualizada =>", lista2)

lista3 = [1,2,3,4]
del lista3[-1]
lista3 = lista3 + [100,200,300]
lista3.insert(1, -1)
print("lista3", lista3)

listaGrande = lista + lista2 + lista3
print("Lista Grande => ", listaGrande)

#==> EJERCICIO 2

""" Determine si el numero 25 está en la lista edades,
    y si es así cuantas veces aparece.
    edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] """

edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

is25inList = (25 in edades)

frecuenciaDel25 = edades.count(25)
print("is25inList => ", is25inList)
print("frecuenciaDel25 => ", frecuenciaDel25)


#==> EJERCICIO 3
""" Teniendo en cuenta la lista anterior, ordene de forma ascendente,luego descendente a los elementos.
    Pero sin alterar la lista edades original. """

edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
edadesCopia = edades.copy()
edadesCopia.sort()
print(edadesCopia)
edadesCopia.sort(reverse=True)
print(edadesCopia)


#==> EJERCICIO 4
""" Cree una copia de edades y haga lo siguiente:
   * Muestre en pantalla el elemento inicial y el final
   * Remueva aquellos elementos cuyo valor es 0 o 1"""

edadesCopia = edades.copy()
print("Elemento inicial y final de edadesCopia =>", edadesCopia[0], edadesCopia[-1])
edadesCopia.remove(0)
edadesCopia.remove(1)
print("edadesCopia => ", edadesCopia)

#==> EJERCICIO 5
"""  Utilice slicing para extraer a partir de la lista edades:
         - Elementos ubicados en indices pares
         - Elementos ubicados en indices impares
         - Todos los elementos, pero al revés de la lista
         - Cada 70avo elemento a partir del 10
         - Cada 100avo elemento, pero al revés de la lista
         - Cada 35avo elemento, a partir de la mitad
  ¿Qué operaciones puedo hacer con listas que no puede hacer con tuplas? """


print("en indices pares=>", edades[0::2])
print("en indices impares=>",  edades[1::2])
print("lista al revés =>",  edades[::-1])
print("cada 70avo elemento =>",  edades[10::70])
print("cada 100avo =>",  edades[::-1][0::100])
print("cada 35avo =>",  edades[int((len(edades)-1)/2)::35])




#====================== EJERCICIOS MÉTODOS DE DICCIONARIOS ====================

#==> EJERCICIO 1
""" Cree el siguiente diccionario =>
    Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}
     
       a) Extraiga los keys y values del diccionario, almacenelos en las variables claves, valores, respectivamente
       b) Corrija en el diccionario las calificaciones de Marly (4.3), Angel (3.1) y Juanita (3.5)
       c) Elimine a los estudiantes Josefina y Juan.
       d) Cree una copia y llamela reprobados, elimine todos aquellos con calificación mayor o igual a 3
       e) Muestre en pantalla la mejor calificación, para ello utilice indexing
       f) Muestre en pantalla la peor calificación, para ello utilice indexing 
       g) Utilice indexing para agregar dos nuevos estudiantes: Marco(3.0) Alejandra(5.0)"""

#a
Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}
claves = Calificaciones.keys()
valores= Calificaciones.values()

#b
Calificaciones["Marly"] = 4.3
Calificaciones["Angel"] = 3.1
Calificaciones["Juanita"] = 3.5

#c
Calificaciones.pop("Josefina")
Calificaciones.pop("Juan")

#d
reprobados = Calificaciones.copy()
for key, value in Calificaciones.items():
       if value >=3:
             reprobados.pop(key)
print("reprobados ==>", reprobados)      

#e
mejorNota = 0
keyMejorNota = ""

for key in Calificaciones.keys():
   if Calificaciones[key] > mejorNota:
      mejorNota = Calificaciones[key]
      keyMejorNota = key

print("mejor calificacion =>", Calificaciones[keyMejorNota])

#f es análogo al anterior

#g)

Calificaciones["Marco"] = 3.0
Calificaciones["Alejandra"] = 5.0


#==> EJERCICIO 2
""" Utilizando diccionarios cree una base de datos de empleados de una empresa,
la base de datos se debe llamar empleadosMabe. Debe contener la siguiente información
Cod   Nombre               Cargo          Salario   
0001   Cristian Pachon     Ingeniero      $ 3.200.000
0002   Daniela Pineda      Programador    $ 4.300.000
0003   Esteban Murcia      Programador    $ 4.600.000
0004   Jose Guzman         Ingeniero      $ 3.900.000
0005   Camilo Rodriguez    Ensamblador    $ 1.200.000
0006   Mariana Londoño     Ensamblador    $ 1.100.000
0007   Estefania Muños     Ensamblador    $ 1.700.000
0008   Cristian Rodriguez  Ingeniero      $ 3.100.000
0009   Natalia Alzate      Ensamblador    $ 2.200.000
0010   Juan Sanabria       Diseñador      $ 5.100.000
0011   Juanita Calderon    Ensamblador    $ 1.300.000
0012   Laura Quintero      Administrador  $ 2.500.000
0013   Viviana Quesada     Guardia        $ 1.500.000
A partir de la base de datos, busque una manera de:
    a) Encontrar la persona con mayor salario
    b) Encontrar la persona con menor salario
    c) Calcular el gasto total de la empresa por motivo salarios
    d) Calcular el promedio de lo que ganan los programadores
    e) Calcular el promedio de lo que ganan los ensambladores"""


empleadosMabe = {
   "codigos" : ["0001","0002","0003","0004","0005","0006","0007","0008","0009","0010","0011","0012","0013"],
   "nombres" : ["Cristian Pachon","Daniela Pineda","Esteban Murcia","Jose Guzman","Camilo Rodriguez","Mariana Londoño","Estefania Muños","Cristian Rodriguez","Natalia Alzate","Juan Sanabria","Juanita Calderon","Laura Quintero","Viviana Quesada"],
   "cargos"  : ["Ingeniero","Programador","Programador","Ingeniero","Ensamblador","Ensamblador","Ensamblador","Ingeniero","Ensamblador","Diseñador","Ensamblador","Administrador","Guardia"],
   "salarios": [3200000,4300000,4600000,3900000,1200000,1100000,1700000,3100000,2200000,5100000,1300000,2500000,1500000]
}


#a
mayorSalario = 0
indiceMayorSalario = 0
contador = 0

for salario in empleadosMabe["salarios"]:
   if salario > mayorSalario:
      mayorSalario = salario
      indiceMayorSalario = contador
   contador += 1

print("mayor salario =>", empleadosMabe["nombres"][indiceMayorSalario])
       
       
#b es analogo

#c 
print("Gasto total salarios =>", sum(empleadosMabe["salarios"]))

#d y e
indicesProgramadores = []
indicesEnsambladores = []
indice = 0   # indice es el indice de la lista cargos

for cargo in empleadosMabe["cargos"]:
   if cargo == "Programador":
      indicesProgramadores.append(indice)
   if cargo == "Ensamblador":
      indicesEnsambladores.append(indice)
   indice += 1

totalSalariosEnsambladores = 0
totalSalariosProgramadores = 0

for indice in indicesEnsambladores:
   totalSalariosEnsambladores += empleadosMabe["salarios"][indice]

for indice in indicesProgramadores:
       totalSalariosProgramadores += empleadosMabe["salarios"][indice]

promedioSalarioProgramadores = totalSalariosProgramadores / len(indicesProgramadores)
promedioSalarioEnsambladores = totalSalariosEnsambladores / len(indicesEnsambladores)

print("promedio Programadores =>", promedioSalarioProgramadores)
print("promedio Ensambladores =>", promedioSalarioEnsambladores)       

     






