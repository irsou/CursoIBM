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

#crear función que descomponga en factores un nº

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


def minimo(l):
    l[0] = 1000
    return minimo(l)

print(minimo(0))

