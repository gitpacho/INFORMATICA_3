columnas = ["Nombre","Cargo","Salario"]
indices = ["0001","0002","0003","0004","0005","0006","0007","0008","0009","0010","0011","0012","0013"]
datos =  [["Cristian Pachon"     ,"Ingeniero"      ,3200000],
          ["Daniela Pineda"      ,"Programador"    ,4300000],
          ["Esteban Murcia"      ,"Programador"    ,4600000],
          ["Jose Guzman"         ,"Ingeniero"      ,3900000],
          ["Camilo Rodriguez"    ,"Ensamblador"    ,1200000],
          ["Mariana Londoño"     ,"Ensamblador"    ,1100000],
          ["Estefania Muños"     ,"Ensamblador"    ,1700000],
          ["Cristian Rodriguez"  ,"Ingeniero"      ,3100000],
          ["Natalia Alzate"      ,"Ensamblador"    ,2200000],
          ["Juan Sanabria"       ,"Diseñador"      ,5100000],
          ["Juanita Calderon"    ,"Ensamblador"    ,1300000],
          ["Laura Quintero"      ,"Administrador"  ,2500000],
          ["Viviana Quesada"     ,"Guardia"        ,1500000]]



dataFrameEmpresa = pandas.DataFrame(index=indices,
                                    columns=columnas,
                                    data=datos
                                    )
print(dataFrameEmpresa)
