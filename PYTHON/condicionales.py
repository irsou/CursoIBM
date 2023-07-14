
#mayor que 5

nota=int(input("Introduzca una nota: "))

if(nota<5):
    evaluacion="suspendido"
else:
    evaluacion="aprobado"
print(evaluacion)

#mayor de 18

edad=int(input("Introduce tu edad: "))
if(edad<18):
    resultado="Tienes prohibida la entrada"
elif (edad>100):
    resultado="Introduce un número correcto"
else:
    resultado="Puedes entrar"
print(resultado)

#evaluacion

nota=int(input("Introduce la nota: "))

if(nota<5):
    evaluacion2="Suspenso"
elif(nota<7):
    evaluacion2="aprobado"
elif(nota<9):
    evaluacion2="notable"
else:
    evaluacion2="sobresaliente"
    
print(evaluacion2)   


#crear diccionario e imprimirlo

keys=['nombre','apellido','edad']
values=['Laura','Diaz','25']
diccio= dict(zip(keys, values))

for k in diccio:
    elemento= '{}: {}'.format(k, diccio[k])
    print(elemento)
    
letras =list('abcdefghijklmnopqrstuvwxyz')

l1=letras[:8]
l2=letras[8:16]
l3=letras[16:]

print(l1)
print(l3)
print(l2)

#baraja las letras
import random
random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)

for a,b,c in zip(l1,l2,l3):
    print (a+b+c, end=' ')

##############################################

letras =list('abcdefghijklmnopqrstuvwxyz')
vocales='aeiou'

random.shuffle(letras)
print(''.join(letras))
print(letras)

for i, letra in enumerate(letras):
    if letra in vocales:
        print('{} en la posición {}'.format(letra,i))
        
        
abcde=sorted(letras) [:5]
print(list(enumerate(abcde)))
print('le decimos por qué número empieza')
print(list(enumerate(abcde,8)))


#crear fichero

zen = '''\
    Bello es mejor que feo. 
    Explícito es mejor que implícito
    Simple es mejor que complejo
    '''

f=open('short_zen.txt','w')
f.writelines(zen)
f.close()

f=open('short_zen.txt','r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
f.close()

print('***************')

for linea in open('short_zen.txt'):
    print(linea.upper(), end=' ')
    
print('***************')

for linea in open('short_zen.txt'):
    print(linea.upper())

print('***************')
f=open('short_zen.txt','r')

print(next(f))
print(next(f))
print(next(f))
print(next(f))
f.close()

# iterador next // iterable iter


#if abreviado

n1=5
n2=3
if n1>n2: print(n1, 'es mayor que', n2)


#if else abreviado
n1=5
n2=3

print(n1, 'es mayor que', n2) if n1>n2 else print(n2, 'es mayor que', n1)

# if 0<edad<100 equivale a if edad>0 and edad<100


for i in [1,10]:
    print("Hola")
    
for i in ["primavera", "verano", "otoño", 
"invierno"]: 
    print(i)
    
print('***************')

for i in ["primavera", "verano", "otoño", 
"invierno"]: 
    print(i)

print('***************')

for i in range(5,10):
    print(f"Valor de la variable {i}")

print('***************')  
for i in range(5,10,2):
    print(f"Valor de la variable {i}")

for x in "banana":
    print(x)
    
for x in "banana":
    print(x, end='')

print('***************') 

frutas = ["manzana", "banana", "cereza"]
#break después de imprimir
for x in frutas:
    print(x)
    if x == "banana":
        break
#break antes de imprimir   
for x in frutas:
    if x == "banana":
        break
    print(x)
    
#continue para saltar banana   
for x in frutas:
    if x == "banana":
        continue
    print(x)

#indicar nº de veces que se ejecuta (fin) 
for x in range(6):
    print(x)
    
#indicar nº de veces que se ejecuta (inicio y fin)
for x in range(2,6):
    print(x)

#indicar nº de veces que se ejecuta (iniciom fin y rango)
for x in range(2,6,3):
    print(x)


#bucle anidado

color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    for y in color:
        print(x, y)
        


edad=int(input('Introduce tu edad: '))

while edad<0:
    print('edad errónea')
    edad=int(input('Introduce tu edad: '))
    
#calcular raíz cuadrada de nº positivo (3 intentos de meter nº)

intentos=0
import math
numRaiz = int(input('Introduce un nº: '))

while numRaiz<0:
    intentos = intentos +1
    print('número erróneo')
    numRaiz = int(input('Introduce un nº: '))
    
    if intentos==2:
        print('máximo de números introducidos') 
        break; 

if numRaiz>=0:
    print('La raíz cuadrada de', numRaiz, 'es',math.sqrt(numRaiz))
    
