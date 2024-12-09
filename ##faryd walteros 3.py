##faryd walteros
##SEGUNDO PUNTO
n = int(input("ingrese un numero : "))

while n != 1 :
    if n%2 == 0:
        n//=2
    else :
        n = n*3+1
        print(n)