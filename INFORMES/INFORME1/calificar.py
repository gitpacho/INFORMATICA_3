from variablesDeEntorno import nombresUsuarios, nombre_repositorio, nombreInforme, archivoDeCalificaciones, nombreArchivo

#-------------solucion de los ejercicios------------
from respuestasCorrectas import funciones, diccionarioPagos, codigosAltosSalarios, parCercano, ventasEmpresa
solucion1, stringVariable1 = funciones, "funciones"
solucion2, stringVariable2 = diccionarioPagos, "diccionarioPagos"
solucion3, stringVariable3 = codigosAltosSalarios, "codigosAltosSalarios"
solucion4, stringVariable4 = parCercano, "parCercano"
solucion5, stringVariable5 = ventasEmpresa, "ventasEmpresa"

#-------------respuestas de los estudiantes------------
import ejercicios1, sys
sys.path.insert(0, "./TEMPORAL/INFORMES/{}".format(nombreInforme))
sys.path.pop(1)

try: respuesta1 = ejercicios1.funciones;
except: print("ADVERTENCIA: respuesta1 ({}) no encontrada".format(stringVariable1))
try: respuesta2 = ejercicios1.diccionarioPagos
except: print("ADVERTENCIA: respuesta2 ({}) no encontrada".format(stringVariable2))
try: respuesta3 = ejercicios1.codigosAltosSalarios
except: print("ADVERTENCIA: respuesta3 ({}) no encontrada".format(stringVariable3))
try: respuesta4 = ejercicios1.parCercano
except: print("ADVERTENCIA: respuesta4 ({}) no encontrada".format(stringVariable4))
try: respuesta5 = ejercicios1.ventasEmpresa
except: print("ADVERTENCIA: respuesta5 ({}) no encontrada".format(stringVariable5))

#------------ funciones para preparar la calificaion------------

def mensajeDeInicio():
    global calificacion, os, sys
    import os
    print("\n----------------------INICIO----------------------")
    input("\nPresione enter para importar el informe: ")
    calificacion = 0
def importarArchivos():
    try:
        import os
        input()
        lineaReporte = "\nImportando ejercicios1.py ..."
        print("\nImportando {} ...".format(nombreArchivo))
        print("ejercicios1.py ha sido importado")
        input()
    except:
        print("WARNING: Archivo ejercicios1.py tiene errores o no existe")
        input("Presione enter para terminar proceso: \n")
        raise Exception 
    try: 
        print("\nImportando nombre del estudiante ...")
        nombreEstudi = ejercicios1.nombre_completo
        print("El estudiante ingresó el nombre: {}".format(nombreEstudi))
        input()
    except: 
        print("warning: el estudiante no almacenó el nombre")
        pregunta = input("Desea calificar aún así: (si/no): ")
        if pregunta == "no":
            raise Exception 
    try:
        print("\nImportando relatoria1.pdf ...")
        os.rename('TEMPORAL/INFORMES/{}/relatoria1.pdf'.format(nombreInforme), 'INFORMES/{}/PDFS/{}.pdf'.format(nombreInforme ,nombreEstudiante.title().replace(" ", "").replace("_", " ").replace("-", " ")))
        print("Relatoria almacenada en carpeta PDFS")
        input()
    except:
        print("warning: Archivo relatoria1.pdf no existe o ya ha sido movido")
        input()

def verificarVariables():
    global v1, v2, v3, v4, v5
    global respuesta1, respuesta2, respuesta3, respuesta4, respuesta5
    v1,v2,v3,v4,v5 =False,False,False,False,False
    print("\nVariables encontradas ===>\n")

    try:
        condicion1 = isinstance(respuesta1, list) 
        condicion2 = len(respuesta1) == 4
        if condicion1 and condicion2: 
            v1 = True
            print("Ejercicio1 ==> {} ✔".format(stringVariable1))
        else:
            print("Ejercicio1 ==> {} ⲭ".format(stringVariable1))
    except:
        print("Ejercicio1 ==> {} ⲭ".format(stringVariable1))
    
    try:
        condicion1 = isinstance(respuesta2, dict)
        condicion2 = len(respuesta2) == 10
        if condicion1 and condicion2:
            v2 = True
            print("Ejercicio2 => {} ✔".format(stringVariable2))
        else:
            print("Ejercicio2 ==> {} ⲭ".format(stringVariable2))
    except:
        print("Ejercicio2 => {} ⲭ".format(stringVariable2))    

    try:
        condicion1 = isinstance(respuesta3, list)
        condicion2 = len(respuesta3) == 3
        if  condicion1 and condicion2:
            v3 = True
            print("Ejercicio3 ==> {} ✔".format(stringVariable3))        
        else:
            print("Ejercicio3 ==> {} ⲭ".format(stringVariable3))
    except:
        print("Ejercicio3 ==> {} ⲭ".format(stringVariable3))
 
    try:
        condicion1 = isinstance(respuesta4, str)
        if  condicion1:
            v4 = True
            print("Ejercicio4 ==> {} ✔".format(stringVariable4))        
        else:
            print("Ejercicio4 ==> {} ⲭ".format(stringVariable4))
    except:
        print("Ejercicio4 ==> {} ⲭ".format(stringVariable4))

    try:
        condicion1 = (type(respuesta5).__name__ == "function")
        if  condicion1:
            v5 = True
            print("Ejercicio5 ==> {} ✔".format(stringVariable5))        
        else:
            print("Ejercicio5 ==> {} ⲭ".format(stringVariable5))
    except:
        print("Ejercicio5 ==> {} ⲭ".format(stringVariable5))
    
def mensajeCalificarEjercicios():
    input("\nPresione enter para ver los resultados ...")
    print("\n\n-----------------RESULTADOS-----------------------\n")  

def realizarInforme():
    import json
    print("\n------------  INFORME -----------------")
    input("\n Presione enter para almacenar resultados")
    print("\n Calificación {} ==========>".format(nombreEstudiante), round(calificacion, 2))
    with open("INFORMES/{}/{}".format(nombreInforme, archivoDeCalificaciones), "r") as file:
        DATA = json.load(file)
    DATA[nombreEstudiante] = round(calificacion, 2)
    with open("INFORMES/{}/{}".format(nombreInforme, archivoDeCalificaciones), "w") as file:
        DATA = json.dump(DATA, file)
def calificarEjercicios():
    global calificacion

    if v1:
        input()
        print("\n============== PUNTO1 ===============> \n\n>>")
        print("\n>> RESPUESTA CORRECTA:   {}".format(solucion1), "\n")
        print("\n>> RESP ESTUDIANTE:   {}".format(respuesta1), "\n")
        try:
            if (solucion1[0] == respuesta1[0]):
                calificacion += 1.0/3
                print("\n --Correcto--", "+0.33")
            else:
                print("\n --Incorrecto--", "+0")
            if solucion1[1] == respuesta1[1]:
                calificacion += 1/3
                print(" --Correcto--", "+0.33")
            else:
                print(" --Incorrecto--", "+0")
            if solucion1[2] == respuesta1[2]:
                calificacion += 1/3
                print(" --Correcto--", "+0.33")
            else:
                print(" --Incorrecto--", "+0")          
        except:
            print("\n>> RESP ESTUDIANTE:   {}".format("Tiene errores"))
            print("--Incorrecto--", "+0")

    if v2:
        input()
        print("\n============== PUNTO2 ===============> \n\n>>")
        print("\n>> RESPUESTA CORRECTA:   {}".format(solucion2[0]), "\n")
        print("\n>> RESP ESTUDIANTE:   {}".format(respuesta2), "\n")
        try:
            if (respuesta2 in solucion2):
                calificacion += 1.0
                print("\n --Correcto--", "+1.0")
            else:
                print("\n --Incorrecto--", "+0")
            
        except:
            print("\n>> RESP ESTUDIANTE:   {}".format("Tiene errores"))
            print("--Incorrecto--", "+0")

    if v3:
        input()
        print("\n============== PUNTO3 ===============> \n\n>>")
        print("\n>> RESPUESTA CORRECTA:   {}".format(solucion3), "\n")
        print("\n>> RESP ESTUDIANTE:   {}".format(respuesta3), "\n")
        try:
            if (respuesta3[0] == solucion3[0]):
                calificacion += 1/3
                print("\n --Correcto--", "+0.33")
            else:
                print("\n --Incorrecto--", "+0")
            if (respuesta3[1] == solucion3[1]):
                calificacion += 1/3
                print("\n --Correcto--", "+0.33")
            else:
                print("\n --Incorrecto--", "+0")
            if (respuesta3[2] == solucion3[2]):
                calificacion += 1/3
                print("\n --Correcto--", "+0.33")
            else:
                print("\n --Incorrecto--", "+0")
            
        except:
            print("\n>> RESP ESTUDIANTE:   {}".format("Tiene errores"))
            print("--Incorrecto--", "+0")

    if v4:
        input()
        print("\n============== PUNTO4 ===============> \n\n>>")
        print("\n>> RESPUESTA CORRECTA:   {}".format(solucion4), "\n")
        print("\n>> RESP ESTUDIANTE:   {}".format(respuesta4), "\n")
        try:
            if (solucion4 == respuesta4):
                calificacion += 1.0
                print("\n --Correcto--", "+1.0")
            else:
                print("\n --Incorrecto--", "+0")
        except:
            print("\n>> RESP ESTUDIANTE:   {}".format("Tiene errores"))
            print("--Incorrecto--", "+0")
    
    if v5:
        input()
        print("\n============== PUNTO5 ===============> \n\n>>")
        print("\n>> RESPUESTA CORRECTA:   {}".format(solucion5), "\n")
        print("\n>> RESP ESTUDIANTE:   {}".format(respuesta5), "\n")
        try:
            if (respuesta5[0] == solucion5[0]):
                calificacion += 1/4
                print("\n --Correcto--", "+0.25")
            else:
                print("\n --Incorrecto--", "+0")
            if (respuesta5[1] == solucion5[1]):
                calificacion += 1/4
                print("\n --Correcto--", "+0.25")
            else:
                print("\n --Incorrecto--", "+0")
            if (respuesta5[2] == solucion5[2]):
                calificacion += 1/4
                print("\n --Correcto--", "+0.25")
            else:
                print("\n --Incorrecto--", "+0")
            if (respuesta5[3] == solucion5[3]):
                calificacion += 1/4
                print("\n --Correcto--", "+0.25")
            else:
                print("\n --Incorrecto--", "+0")
            
        except:
            print("\n>> RESP ESTUDIANTE:   {}".format("Tiene errores"))
            print("--Incorrecto--", "+0")
def descargarRepositorio():
    import os, shutil
    global nombreEstudiante
    user = input("\n * Ingrese gitHub user: ")
    nombreEstudiante = nombresUsuarios[user]
    os.system("rm -rf TEMPORAL")
    
    repoGit = os.system("git clone https://github.com/{}/{} ./TEMPORAL".format(user, nombre_repositorio))
    if repoGit == 0:
        print("\n -----Repositorio descargado -----\n")
        salida = os.system("ls TEMPORAL/INFORMES/*")
    else: 
        print("\n\n----- No es posible descargar repo -----\n\n")
        raise Exception

if __name__ == "__main__":
    respuesta = input(" ¿? Desea descargar nuevo repositorio: (s/n): ")
    if respuesta == "s":descargarRepositorio()
    else: print("MENSAJE: Asegurese haya un repositorio en TEMPORAL")
    mensajeDeInicio()
    importarArchivos()
    try:
        verificarVariables()
        mensajeCalificarEjercicios()
        calificarEjercicios()
    except:
        print("problemas con los archivos solicitados")

    realizarInforme()