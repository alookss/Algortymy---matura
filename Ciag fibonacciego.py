n=int(input("Podaj liczbe: "))


def FibRek(n):
    if n < 3:
        return 1
    else:
        return FibRek(n-1) + FibRek(n-2)
   

def FibIter(n):
    i=1
    j=1
    for x in range(3,n+1):
        tmp=j
        j=i+j
        i=tmp
    return j

print("Rekurencyjnie:", FibRek(n))
print("Iteracyjnie:", FibIter(n))

  

