
# Dados dos números, escriba un código Python para encontrar el mínimo de estos dos número

a=-1
b=-4

if (a<b):
    menor = a
else: menor=b

print('El número', menor, 'es menor')


#Invertir palabras de una cadena dada.

def inversa(str):
    palabraInvert=str.split()[::-1]
    fraseInvert=' '.join(palabraInvert)
    return(fraseInvert)

str= 'código de práctica de prueba de geeks'
print (inversa(str))


# Realizar una suma de los elementos de una tupla

datos_tupla = (7,8,9,1,10,7)

suma= sum(datos_tupla)

print(suma)

#Escriba un código que desordene al azar una lista.

import random
lista = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(lista)

print(lista)


#Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.

f=open('short_zen.txt','r')
contenido=f.read()
mayusc =0
for element in contenido:
    if element.isupper():
        mayusc +=1

print (mayusc)
f.close()

# Escriba un programa para producir la serie Fibonacci en Python. 

a=0
b=1
veces =int(input('Introduce el nº elementos de la secuencia: '))

secuencia=[a,b]
i=0
while(i<(veces-2)):
    i=i+1
    suma=a+b
    secuencia.append(suma)    
    a =b
    b=suma

print(secuencia)  

    
# Escriba un programa en Python para comprobar si un número es primo.
   
def isPrimo(num):
    if num<1:
        return 'Introduzca un número mayor que cero'
    elif num==2:
        return True
    else:
        for i in range (1, num):
            if num % i==0:
                return False
        return True


num=int(input('Introduce un número: '))
res=isPrimo(num)   
if res=='Introduzca un número mayor que cero':
    print (res)
elif res is True:
    print('Es un número primo')
else: print('No es un número primo')
        
#Escribir un programa en Python para comprobar si un número es capicúa.

num2=input('Introduce un número: ')
numInvert=num2[::-1]

if num2==numInvert:
    print('Es un número capicúa')
else: print('No es capicúa')


