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

#==> EJERCICIO 4
""" Cree una copia de edades y haga lo siguiente:
   * Muestre en pantalla el elemento inicial y el final
   * Remueva aquellos elementos cuyo valor es 0 o 1"""
 
#==> EJERCICIO 5
"""  Utilice slicing para extraer a partir de la lista edades:
         - Elementos ubicados en indices pares
         - Elementos ubicados en indices impares
         - Todos los elementos, pero al revés de la lista
         - Cada 70avo elemento a partir del 10
         - Cada 100avo elemento, pero al revés de la lista
         - Cada 35avo elemento, a partir de la mitad
  ¿Qué operaciones puedo hacer con listas que no puede hacer con tuplas? """