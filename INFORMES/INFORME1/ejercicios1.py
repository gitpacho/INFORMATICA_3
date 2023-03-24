nombre_completo = ""   #Por favor ingrese su nombre COMPLETO en la cadena

"""
Recomendaciones:
 - No imprimir las respuestas al momento de entregar su archivo
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
"""



#------------------------ EJERCICIO 1 ----------------------------------------------------------------------------------

"""Definir las siguientes funciones: 

NOMBRE DE LA FUNCION      PARAMETRO DE ENTRADA     VALOR DE RETORNO       PROBLEMA
* esMayorDeEdad            * edad (entero +)         * booleano        * Función que determine si una persona es mayor de edad.   Ej: 29 => True
* sumadeDigitos            * numero (entero +)       * entero          * Función que calcule la suma de los digitos de un numero. Ej: 921 =>  12 
* tieneVocales             * mensaje (string)        * booleano        * Función que determine si un mensaje tiene vocales o no.  Ej: "hola" => True
* esPrimo                  * numero  (entero +)      * booleano        * Función para determinar si un número es primo.           Ej: 20 => False

Entregue la respuesta en una lista llamada funciones, copiando la siguiente linea =>
funciones = [esMayorDeEdad, sumadeDigitos, tieneVocales, esPrimo] 
"""

#------------------------ EJERCICIO 2 ----------------------------------------------------------------------------------
""" Diez compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. 
Se prestarán dos servicios al día, uno de ida y el otro de regreso.

Sin embargo, los diez no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre todos.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:

                              IDA                             |                       REGRESO
              LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     |    LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
"Mariana"       Si        No        Si      No      No        |      No        No        Si      No       No
"Sofia"         Si        No        No      Si      Si        |      Si        No        No      Si       No
"Camila"        Si        No        Si      No      Si        |      No        No        No      No       No
"Maria"         Si        Si        Si      No      No        |      No        No        Si      No       No
"Juan"          Si        Si        Si      Si      No        |      Si        No        Si      No       No
"Angie"         Si        No        Si      No      No        |      Si        No        Si      No       No
"Esteban"       Si        No        No      Si      Si        |      No        No        No      Si       No
"Jose"          Si        No        Si      Si      No        |      Si        No        Si      Si       No
"Gisell"        Si        Si        No      Si      No        |      Si        No        Si      No       No
"Cristian"      Si        Si        Si      No      No        |      Si        Si        Si      No       No

¿Cuanto debe pagar cada estudiante? 

Almacene el resultado dentro de un diccionario llamado => diccionarioPagos
las claves deben ser los nombres de los estudiantes (en strings)
y los valores deben ser el dinero total que pagó cada uno al terminar la semana (2 decimales, use round())
"""


#------------------------ EJERCICIO 3 ----------------------------------------------------------------------------------
""" El salario de un empleado de una empresa se calcula, utilizando como base  
$1200000 más la comisión, de acuerdo a las ventas de los siguientes productos:
           
            precio_unidad  comisión
* Pantalon:   $ 38 000        3%
* Zapatos:    $ 55 500        5%
* Tenis:      $ 71 000        4%  
* Camisa:     $ 29 500        2%
* Corbata:    $ 25 000        7%
* Blusas:     $ 80 500        5%
* Vestidos:   $ 95 000        2%

 Determine el codigo de los 3 empleados con mayor salario en la empresa,
 si las ventas fueron las siguientes:

                  |                     UNIDADES VENDIDAS        
CODIGO_EMPLEADO   |  zapatos tenis camisas corbatas pantalones blusas vestidos 
     "001"        |    20      22     30      2        40        20      3    
     "002"        |    31      14     32      15       13        20      11   
     "010"        |    24      32     40      9        12        50      13   
     "020"        |    42      12     33      24       22        32      23   
     "021"        |    51      21     25      10       19        14      2    
     "022"        |    22      31     51      21       35        15      11   
     "023"        |    21      36     22      32       39        32      15   
     "024"        |    22      33     41      21       43        31      36   
     "025"        |    33      31     20      42       33        42      35   
     "031"        |    22      47     5       28       37        31      32   
     "032"        |    24      38     33      21       41        31      16   
     "033"        |    21      18     32      37       39        22      12   
     "041"        |    33      31     21      21       33        39      25   
     "042"        |    25      39     20      48       15        30      32   
     "043"        |    27      32     29      28       37        35      16   
     "121"        |    24      12     31      21       39        32      13   
     "122"        |    31      31     50      22       13        30      21   
     "123"        |    23      35     35      39       31        19      19   
     "351"        |    26      36     39      27       35        32      16   
     "352"        |    25      31     21      21       25        37      15   
     "353"        |    23      34     35      32       37        20      49   
     "368"        |    31      14     29      39       25        37      16   
     "369"        |    26      31     31      27       37        32      41   
     "461"        |    40      42     23      11       21        15      19   
     "466"        |    27      31     39      21       31        32      25   
     "469"        |    38      32     19      29       35        50      16    

Almacene los códigos en una lista llamada => codigosAltosSalarios
"""

#------------------------ EJERCICIO 4 ----------------------------------------------------------------------------------
"""
Dados los siguientes puntos geométricos:
"P1" ==> (5, 2, 3)             P11 ==>  (2, 2, 3)
"P2" ==> (4, 1, 3)             P12 ==>  (2, 3, 4)
"P3" ==> (2.5, 1, 0)           P13 ==>  (1, 1, 3)
"P4" ==> (0.5, 0.5, 2)         P14 ==>  (4, 4, 4)
"P5" ==> (1, 2, 1)             P15 ==>  (5, 5, 1)
"P6"  ==> (6, 2, 1)            P16 ==>  (1, 0.5, 1)
"P7"  ==> (3, 2, 0.5)          P17 ==>  (3, 4, 5)
"P8"  ==> (2, 6, 1)            P18 ==>  (3, 1, 2)
"P9"  ==> (0, 0, 0)            P19 ==>  (3, 9, 1)
"P10" ==> (2, 0, 0.5)          P20 ==>  (0.5, 0.5, 6)

Determine el par de puntos que se encuentran más cercanos.
Almacene la respuesta en un string llamado parCercano. Ejemplo:
parCercano = "P3-P10" 
"""

#------------------------ EJERCICIO 5 ----------------------------------------------------------------------------------

"""El precio de venta de los artículos de una empresa es el siguiente:
                            
                            Codigo      Precio unitario
                             A001          $ 31 000
                             A011          $ 25 000
                             A032          $ 43 000
                             A125          $ 55 000
                             B001          $ 10 000
                             B005          $ 20 000
                             P009          $ 30 000
                             P019          $ 49 000
                             R001          $ 60 000
                             W307          $ 90 000
                             Z052          $ 35 000
                             Z025          $ 27 000
                             Z278          $ 65 000

Las ventas a lo largo de un día se ha registrado en la siguiente lista =>
registros = ["P009-21Unidades", "B005-19Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades", "A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades" ]

Cree una función llamada ==> ventasEmpresa
Que reciba como parámetro de entrada la lista => registros
Que retorne el dinero_total recaudado por la empresa a lo largo del día

def ventasEmpresa(registros):
    ....
    return dinero_total
"""