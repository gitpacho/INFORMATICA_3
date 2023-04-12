columnas = ["Nombre","Cargo","Salario", "Años_experiencia"]
indices = ["0001","0002","0003","0004","0005","0006","0007","0008","0009","0010","0011","0012","0013"]
datos =  [["Cristian Pachon"     ,"Ingeniero"      ,3200000, 8],
          ["Daniela Pineda"      ,"Programador"    ,4300000, 9],
          ["Esteban Murcia"      ,"Programador"    ,4600000, 10],
          ["Jose Guzman"         ,"Ingeniero"      ,3900000, 8],
          ["Camilo Rodriguez"    ,"Ensamblador"    ,1200000, 2],
          ["Mariana Londoño"     ,"Ensamblador"    ,1100000, 1],
          ["Estefania Muños"     ,"Ensamblador"    ,1700000, 5],
          ["Cristian Rodriguez"  ,"Ingeniero"      ,3100000, 8],
          ["Natalia Alzate"      ,"Ensamblador"    ,2200000, 6],
          ["Juan Sanabria"       ,"Diseñador"      ,5100000, 11],
          ["Juanita Calderon"    ,"Ensamblador"    ,1300000, 4],
          ["Laura Quintero"      ,"Administrador"  ,2500000, 7],
          ["Viviana Quesada"     ,"Guardia"        ,1500000, 3]]

import pandas
dataFrameEmpresa = pandas.DataFrame(index=indices,
                                    columns=columnas,
                                    data=datos
                                    )
print(dataFrameEmpresa)


#Graficar la dispersion => Años_experiencia vs salario
#Graficar el histograma => salario
#graficar el histograma => Años_experiencia
#graficar el diagrama de barras => cargo vs salario_promedio

import matplotlib.pyplot as plt

x = dataFrameEmpresa["Años_experiencia"].values
y = dataFrameEmpresa["Salario"].values
plt.figure()
plt.plot(x, y, "or", label = "Dispersion")
plt.title(r"$Años\ vs\ Salario$")
plt.xlabel(r"$Años$")
plt.ylabel(r"$Salario$")
plt.grid()
plt.legend()
plt.savefig("figura1.png")
#plt.show()


data = dataFrameEmpresa["Salario"].values
plt.figure()
plt.hist(data, bins = 6)
plt.title(r"$Histograma\ Salarios$")
plt.xlabel(r"$Salario\ [millones]$")
plt.ylabel(r"$Frecuencia\ [unidades]$")
plt.grid()
plt.savefig("figura2.png")
#plt.show()


extraccion = dataFrameEmpresa[["Cargo", "Salario"]].groupby(["Cargo"]).mean()
cargos = extraccion.index
promedios = extraccion["Salario"]

plt.figure()
plt.bar(cargos, promedios)
plt.title(r"$Diagrama\ De\ Barras$")
plt.xlabel("Cargos")
plt.ylabel("Salario promedio")
plt.xticks(rotation='vertical')
plt.savefig("figura3.png")
#plt.show()




#Ejercicios ===>  

"""
Realizar un diagrama de barras del rendimiento vs edad
-------------- Deportista_1  Deportista_2  Deportista_3  Deportista_4  Deportista_5  Deportista_6  Deportista_7  Deportista_8  Deportista_9  Deportista_10  Deportista_11  Deportista_12  Deportista_13  Deportista_14  Deportista_15  Deportista_16  Deportista_17  Deportista_18  Deportista_19  Deportista_20  Deportista_21  Deportista_22  Deportista_23  Deportista_24  Deportista_25  Deportista_26  Deportista_27 
Rendimiento --    "A"           "B"           "C"            "B"            "B"           "B"          "C"           "B"             "A"           "C"          "B"          "A"             "C"             "B"          "B"              "B"           "B"             "A"           "B"            "A"           "A"             "C"             "B"             "B"          "B"            "B"            "C"             
Edad ---------     42            60            18             20             35            25           60            30              19            42           21           17              39              30           28               34            27              23            23             20            25             "40"             31             32            45             26             17             
"""





