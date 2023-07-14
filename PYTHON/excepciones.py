

a=10
b=5

assert(a<b), 'A es mayor que B'

class miExcepcion(Exception):
    pass

try:
    raise miExcepcion
except miExcepcion:
    print('He capturado mi excepción')


class miError(Exception):
    
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return str(self.valor)

raise(miError('Mensaje de error'))