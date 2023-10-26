import math

a=int(input('Podaj a: '))
b=int(input('Podaj b: '))
c=int(input('Podaj c: '))

delta=(b*b -4*a*c)
print('Delta: ', delta)

if delta<0:
    print('Równanie nie ma pierwiastków')
elif delta>0:
    delta_square=(math.isqrt(delta))
    print('Pierwiastek z delty: ', delta_square)
    print('Równanie ma dwa pierwiastki')
    print('x1=', (-b + delta_square)/ 2*a)
    print('x2=', (-b - delta_square)/ 2*a)
else:
    print('Pierwiastek z delty: ', delta_square)
    print('Równanie ma jeden pierwiastek')
    print('x0=', -b/2*a)
