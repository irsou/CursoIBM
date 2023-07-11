
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