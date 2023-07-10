edad=47
MICTE=3.1416
text1='Hola Mundo'
text2='365'
miBoolean=True
print(text2)


# forzado de tipos//casting

x=str('Hello World')
x=int(20)
x=float(20.5)
x=list(("apple","banana","cherry"))
x=tuple(("apple","banana","cherry"))
dx=range(6)
x=dict(name="John", age=36)
x=set(("apple","banana","cherry"))
x=bool(5)

y=int(2.8) 
# y valdrá 2
y=int("3")
# y valdrá 3 
z=float("4")
#  z valdrá 4.0
y=str(3.0)
# y valdrá '3.0'

# para concatenar con + no puedes mezclar tipos de variables y le tienes que meter los espacios " ". La , te concatena todo y mete tdo

print("Hola," + str(x) + "jajaja")
print("Hola", x, "jajaja")

# edad = input ("Introduzca su edad")
# #  la variable de un input siempre es str, hay que castear si se quiere otro tipo

# edad=int(input("Introduzca su edad: "))


def suma (a,b):
    return a+b

def imprimir(frase1, frase2):
    print(frase1,frase2)
    

def f1(a):
    print(a)
    b=100
    def f2(x):
        print(x)

    f2(b)
    
    
f1('Python')

#recursividad_ factorial de un número

def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
    
print(factorial(6))

def factores(x):
    factores =[]
    divisor=2
    
    
    while x>1:
        if x%divisor==0:
            factores.append(divisor)
            x=x/divisor
        else:
            divisor+= 1
    
    return factores

print(factores(126))      

    
