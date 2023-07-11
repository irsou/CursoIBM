
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