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


