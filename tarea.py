#datos de la nomina
nominaDatos=4

def creacion_matriz(filas,columnas):
    i=0
    #numero de filas 
    matriz=[None]*filas
    print(matriz)
    #columnas
    while i < filas:
        matriz[i]=[None]*columnas
        i+=1
        print(matriz)
    return matriz        
#llamada de la creacion de la matriz
#se elige la cantidad de espacio en los parametros
#Filas sera el id y columnas los datos
#lectura e introduccion de datos

def lid(matriz, filas, columnas):
    i = 0
    while i < filas:
        j = 0
        while j < 3:
            print("Empleado",i+1)
            if j==0:
                print("Ingrese, el nombre del trabajador: ")
            elif j==1:
                print("Ingrese los dias trabajados")
            elif j==2:
                print("Ingrese el sueldo basico")
            if j==0:
                matriz[i][j] = (input())
            else:
                matriz[i][j] = int((input()))   
            #if j 0
            j += 1
            print("Columna (j):", j)
            print("Fila (i):", i)
        

        i += 1
    return matriz
def sueldototal(matriz, filas):
    i = 0
    while i < filas:
        dias = matriz[i][1]          
        sueldo_basico = matriz[i][2]  
        
        #resultado en la columna 3
        matriz[i][3] = (sueldo_basico / 30) * dias
        
        i += 1
    return matriz

def principal():
    filas = int(input("Cuántos trabajadores hay?: "))
    columnas = nominaDatos
    
    mi_matriz = creacion_matriz(filas, columnas)
    mi_matriz = lid(mi_matriz, filas, columnas)
    mi_matriz = sueldototal(mi_matriz, filas)

    print(mi_matriz)
    
    #Generamos el archivo de text
    guardar_archivo(mi_matriz, filas)



def guardar_archivo(matriz, filas):
    #crea el archivo nomina.txt
    with open("nomina.txt", "w", encoding="utf-8") as archivo:
        archivo.write("           REPORTE DE NÓMINA            \n")
        
        i = 0
        while i < filas:
            nombre = matriz[i][0]
            dias = matriz[i][1]
            sueldo_basico = matriz[i][2]
            sueldo_total = matriz[i][3]
            
            #los datos del empleado en una línea
            linea = f"Empleado: {nombre} | Días: {dias} | Sueldo Base: ${sueldo_basico} | Total a Pagar: ${sueldo_total:.2f}\n"
            archivo.write(linea)
            
            i += 1

principal()