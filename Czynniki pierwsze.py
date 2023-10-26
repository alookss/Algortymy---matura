liczba=int(input('Podaj liczbe: '))


def pierwsze(x):
    lista = []
    y = 2
    while x > 1:
        while x % y == 0:
            lista.append(y)
            x=x//y
        y += 1

    return lista

print(pierwsze(liczba))

