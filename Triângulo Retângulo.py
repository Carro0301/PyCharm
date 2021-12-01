import math
co=float(input('Digite o valor do Cateto Oposto: '))
ca=float(input('Digite o valor do Cateto Adjacente: '))
hi=math.hypot(co,ca)
print('A hipotenusa medirá {:.2f}'.format(hi))