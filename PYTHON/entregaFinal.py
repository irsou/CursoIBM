
import random

# Crear función que genere matriz y sume filas y columnas

def generar_matriz(n):
    # Creación de matriz
    
    matriz = []

    for i in range(n):
        fila= []
        for j in range(n):
            fila.append(random.randint(0,9))
        matriz.append(fila)
            
    #cálculo suma de filas

    for fila in matriz:
        print(fila)
        lista_suma_f= []

    for fila in matriz:
        suma_fila =  sum(fila)
        lista_suma_f.append(suma_fila)
   
    print("La suma de las filas es",lista_suma_f)


    #cálculo suma de columnas
    lista_suma_c=[]

    for j in range(n):
        suma_columna=0 
        for fila in matriz:
            suma_columna=suma_columna+fila[j]
        lista_suma_c.append(suma_columna)
    
    print("La suma de las columnas es",lista_suma_c) 
    



# Solicitud extensión matriz: se solicita al usuario un número. Si no es dato válido se muestra mensaje de error. Si es dato valido, se llama a la función para generar matriz.

while True:
    try:
        n = int(input("Por favor, introduce el número de filas y columnas de la matriz: "))
        if n<=0:
            raise ValueError
            
        else: generar_matriz(n) 
         
    except ValueError:
        print("Debes introducir un número entre 0 y 99")


      
        
            
            
        








    
