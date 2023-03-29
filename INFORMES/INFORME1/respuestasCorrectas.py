#111111111111111111111111111111111111111111
def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    return False
def sumadeDigitos(numero):
  suma = 0
  for digito in str(numero):
    suma += int(digito)
  return suma
def tieneVocales(mensaje):
  for letra in mensaje:
    if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
      return True
  return False
def esPrimo(numero): #Sirve para evaluar desde el numero 2 en adelante
  for divisor in range(2,numero):
    if (numero % divisor) == 0:
      return False
  return True  
funciones = [esMayorDeEdad, sumadeDigitos, tieneVocales, esPrimo]

#22222222222222222222222222222222222222222222222222222

tarifa1 = 15_000
tarifa2 = 10_000
numeroEstudiantes = 10
nombres = ["Mariana","Sofia","Camila","Maria","Juan","Angie","Esteban","Jose","Gisell","Cristian"]
asistencia = [[True, False,  True,  False,  False,  False,  False,  True,   False,  False],
              [True, False,  False, True,   True,   True,   False,  False,  True,   False],
              [True, False,  True,  False,  True,   False,  False,  False,  False,  False],
              [True, True,   True,  False,  False,  False,  False,  True,   False,  False],
              [True, True,   True,  True,   False,  True,   False,  True,   False,  False],
              [True, False,  True,  False,  False,  True,   False,  True,   False,  False],
              [True, False,  False, True,   True,   False,  False,  False,  True,   False],
              [True, False,  True,  True,   False,  True,   False,  True,   True,   False],
              [True, True,   False, True,   False,  True,   False,  True,   False,  False],
              [True, True,   True,  False,  False,  True,   True,   True,   False,  False]]


personasPorDia = []
for dia in range(10):
  sum = 0
  for estudiante in range(10):
    sum += asistencia[estudiante][dia]
  personasPorDia.append(sum)
pagos = []
for estudiante in range(10):
  pago = 0
  for dia in range(10):
    if asistencia[estudiante][dia]:
      pago += tarifa1 / personasPorDia[dia]
    elif personasPorDia[dia] == 0:
      pago += tarifa2 / numeroEstudiantes
  pagos.append(round(pago,2))
diccionarioPagos = dict(zip(nombres, pagos))


#333333333333333333333333333333333

comisiones = {"Zapatos" : 55500 * 0.05,"Tenis" : 71000 * 0.04,"Camisa" : 29500 * 0.02,"Corbata" : 25000 * 0.07,"Pantalon" : 38000 * 0.03,"Blusas" : 80500 * 0.05,"Vestidos" : 95000 * 0.02}
productos = ["Zapatos","Tenis","Camisa","Corbata","Pantalon","Blusas","Vestidos"]
ventas =  {
"001" :  {"Zapatos": 20, "Tenis": 22,  "Camisa":30,    "Corbata":2,      "Pantalon":  40, "Blusas":  20, "Vestidos": 3},    
"002" :  {"Zapatos": 31, "Tenis": 14,  "Camisa":32,    "Corbata":15,     "Pantalon":  13, "Blusas":  20, "Vestidos": 11},   
"010" :  {"Zapatos": 24, "Tenis": 32,  "Camisa":40,    "Corbata":9,      "Pantalon":  12, "Blusas":  50, "Vestidos": 13},   
"020" :  {"Zapatos": 42, "Tenis": 12,  "Camisa":33,    "Corbata":24,     "Pantalon":  22, "Blusas":  32, "Vestidos": 23},   
"021" :  {"Zapatos": 51, "Tenis": 21,  "Camisa":25,    "Corbata":10,     "Pantalon":  19, "Blusas":  14, "Vestidos": 2} ,   
"022" :  {"Zapatos": 22, "Tenis": 31,  "Camisa":51,    "Corbata":21,     "Pantalon":  35, "Blusas":  15, "Vestidos": 11},   
"023" :  {"Zapatos": 21, "Tenis": 36,  "Camisa":22,    "Corbata":32,     "Pantalon":  39, "Blusas":  32, "Vestidos": 15},   
"024" :  {"Zapatos": 22, "Tenis": 33,  "Camisa":41,    "Corbata":21,     "Pantalon":  43, "Blusas":  31, "Vestidos": 36},   
"025" :  {"Zapatos": 33, "Tenis": 31,  "Camisa":20,    "Corbata":42,     "Pantalon":  33, "Blusas":  42, "Vestidos": 35},   
"031" :  {"Zapatos": 22, "Tenis": 47,  "Camisa":5,     "Corbata":28,     "Pantalon":  37, "Blusas":  31, "Vestidos": 32},   
"032" :  {"Zapatos": 24, "Tenis": 38,  "Camisa":33,    "Corbata":21,     "Pantalon":  41, "Blusas":  31, "Vestidos": 16},   
"033" :  {"Zapatos": 21, "Tenis": 18,  "Camisa":32,    "Corbata":37,     "Pantalon":  39, "Blusas":  22, "Vestidos": 12},   
"041" :  {"Zapatos": 33, "Tenis": 31,  "Camisa":21,    "Corbata":21,     "Pantalon":  33, "Blusas":  39, "Vestidos": 25},   
"042" :  {"Zapatos": 25, "Tenis": 39,  "Camisa":20,    "Corbata":48,     "Pantalon":  15, "Blusas":  30, "Vestidos": 32},   
"043" :  {"Zapatos": 27, "Tenis": 32,  "Camisa":29,    "Corbata":28,     "Pantalon":  37, "Blusas":  35, "Vestidos": 16},   
"121" :  {"Zapatos": 24, "Tenis": 12,  "Camisa":31,    "Corbata":21,     "Pantalon":  39, "Blusas":  32, "Vestidos": 13},   
"122" :  {"Zapatos": 31, "Tenis": 31,  "Camisa":50,    "Corbata":22,     "Pantalon":  13, "Blusas":  30, "Vestidos": 21},   
"123" :  {"Zapatos": 23, "Tenis": 35,  "Camisa":35,    "Corbata":39,     "Pantalon":  31, "Blusas":  19, "Vestidos": 19},   
"351" :  {"Zapatos": 26, "Tenis": 36,  "Camisa":39,    "Corbata":27,     "Pantalon":  35, "Blusas":  32, "Vestidos": 16},   
"352" :  {"Zapatos": 25, "Tenis": 31,  "Camisa":21,    "Corbata":21,     "Pantalon":  25, "Blusas":  37, "Vestidos": 15},   
"353" :  {"Zapatos": 23, "Tenis": 34,  "Camisa":35,    "Corbata":32,     "Pantalon":  37, "Blusas":  20, "Vestidos": 49},   
"368" :  {"Zapatos": 31, "Tenis": 14,  "Camisa":29,    "Corbata":39,     "Pantalon":  25, "Blusas":  37, "Vestidos": 16},   
"369" :  {"Zapatos": 26, "Tenis": 31,  "Camisa":31,    "Corbata":27,     "Pantalon":  37, "Blusas":  32, "Vestidos": 41},   
"461" :  {"Zapatos": 40, "Tenis": 42,  "Camisa":23,    "Corbata":11,     "Pantalon":  21, "Blusas":  15, "Vestidos": 19},   
"466" :  {"Zapatos": 27, "Tenis": 31,  "Camisa":39,    "Corbata":21,     "Pantalon":  31, "Blusas":  32, "Vestidos": 25},   
"469" :  {"Zapatos": 38, "Tenis": 32,  "Camisa":19,    "Corbata":29,     "Pantalon":  35, "Blusas":  50, "Vestidos": 16} }
comisionTrabajador = []
codigoTrabajador = []
for codigo in ventas.keys():
  codigoTrabajador.append(codigo)
  total = 0
  for producto in productos:
    total += ventas[codigo][producto] * comisiones[producto]
  comisionTrabajador.append(total)
#print(codigoTrabajador)
#print(comisionTrabajador)
mayor1, indice1 = -1, -1
mayor2, indice2 = -2, -2
mayor3, indice3 = -3, -3
for indice, comision in enumerate(comisionTrabajador):
  if comision >= mayor1:
    mayor3,indice3 = mayor2, indice2
    mayor2, indice2 = mayor1, indice1
    mayor1,indice1 = comision, indice
    #print("---caso1----")
    #print(indice1, mayor1, " ===> mayor1")
    #print(indice2, mayor2, " ===> mayor2")
    #print(indice3, mayor3, " ===> mayor3")
  elif comision >= mayor2:
    mayor3,indice3 = mayor2, indice2
    mayor2, indice2 = comision, indice
    #print("----caso2----")
    #print(indice1, mayor1, " ===> mayor1")
    #print(indice2, mayor2, " ===> mayor2")
    #print(indice3, mayor3, " ===> mayor3")
  elif comision >= mayor3:
    mayor3, indice3 = comision, indice
    #print("----caso3----")
    #print(indice1, mayor1, " ===> mayor1")
    #print(indice2, mayor2, " ===> mayor2")
    #print(indice3, mayor3, " ===> mayor3")
codigosAltosSalarios = [codigoTrabajador[indice1], codigoTrabajador[indice2], codigoTrabajador[indice3]]
#gananciaComision = [mayor1, mayor2, mayor3]
#print("========>", codigosAltosSalarios, "================")
#print(gananciaComision)



#44444444444444444444444444444444444444444444444444444444444

P1  =  ("P1" ,5, 2, 3)             
P2  =  ("P2" ,4, 1, 3)             
P3  =  ("P3" ,2.5, 1, 0)           
P4  =  ("P4" ,0.5, 0.5, 2)         
P5  =  ("P5" ,1, 2, 1)             
P6  =  ("P6" ,6, 2, 1)            
P7  =  ("P7" ,3, 2, 0.5)          
P8  =  ("P8" ,2, 6, 1)            
P9  =  ("P9" ,0, 0, 0)            
P10 =  ("P10" ,2, 0, 0.5)          
P11 =  ("P11" ,2, 2, 3)
P12 =  ("P12" ,2, 3, 4)
P13 =  ("P13" ,1, 1, 3)
P14 =  ("P14" ,4, 4, 4)
P15 =  ("P15" ,5, 5, 1)
P16 =  ("P16" ,1, 0.5, 1)
P17 =  ("P17" ,3, 4, 5)
P18 =  ("P18" ,3, 1, 2)
P19 =  ("P19" ,3, 9, 1)
P20 =  ("P20" ,0.5, 0.5, 6)
def distancia(PA, PB):
  comparacion = "{}-{}".format(PA[0], PB[0])
  distancia = ((PA[1] - PB[1])**2 + (PA[2] - PB[2])**2 + (PA[3] - PB[3])**2) ** 0.5
  return comparacion, distancia
puntos = [P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,P19,P20]
parCercano = ""
distanciaMinimo = 9999
import itertools
for PA, PB in itertools.combinations(puntos, 2):
  comparacion, distanciaEntrePuntos = distancia(PA, PB)
  if distanciaEntrePuntos <= distanciaMinimo:
    distanciaMinimo = distanciaEntrePuntos
    parCercano =  comparacion
    #print(distanciaEntrePuntos, comparacion)
#print("parCercano", parCercano)


#5555555555555555555555555555555555555555555555555555

precio = {"A001":31000,"A011":25000,"A032":43000,"A125":55000,"B001":10000,"B005":20000,"P009":30000,"P019":49000,"R001":60000,"W307":90000,"Z052":35000,"Z025":27000,"Z278":65000}
registros = ["P009-21Unidades", "B005-19Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades", "A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades" ]
def ventasEmpresa(registros):
  total = 0
  for venta in registros:
    codigo = venta[0:4]
    unidades = venta[5:7]
    total += precio[codigo] * int(unidades)
  return total