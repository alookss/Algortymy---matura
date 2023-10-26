n=int(input("Podaj potege: "))
x=int(input("Podaj liczbe do podniesienia:  "))

def potegarek(x,n):
    if n==1:
        return x
    tmp=potegarek(x,n // 2)
    tmp=tmp*tmp
    if n%2==1:
        tmp=x*tmp
        return tmp
    
print(potegarek(x,n))
