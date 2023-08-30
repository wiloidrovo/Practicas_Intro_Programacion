from random import *

good = True 
#Asignar el número de tanques, y el almacenamiento max y min
while good:
    try: 
        n = int(input("Ingrese la cantidad de tanques: "))
        if (n < 1):
            print('n must be an integer greater than 1')
        min = int(input("min: "))
        max = int(input("max: "))
        if min > max:
            print("Las entradas no son correctas")
        else:
            good = False 
    except:
        print("Las entradas no son correctas.")
X = [0]*n
for i in range (n):
    X[i] = randint(min,max)
print("La capacidad de los tanques son: ", X)

sumX = 0
for i in range(n):
    sumX += X[i]

a = 0
num = 0
Y = [0]*n
i = 0
while a < 1:
    envio = randint(min,max)
    s = max 
    ii = -1
    for k in range(n):
         if (X[k]-envio) >= 0 and (s > X[k]-envio):
             s = X[k] - envio
             ii = k
    if (ii == -1):
        print("El envío ", i+1, " es de ", envio, " y ya no cabe en ningún tanque.")
        break 
    else: 
        Y[ii] = envio
        X[ii] = 0
    print("El envío ", i+1, " es de ", envio, " y fue enviado al tanque ", ii+1)
    i += 1
    num = num+1
    if (i == n):
         a = 1
sumY=0
for i in range (0,n):
    sumY=sumY+Y[i]
espacio_no_usado = sumX - sumY
print("El número de envíos fue: ", num)
print("El contenido de los tanques son: ", Y)
print("La cantidad de espacio total no usado es: ", espacio_no_usado)
