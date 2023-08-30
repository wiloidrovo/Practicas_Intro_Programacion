# Método Simpson 1/3 completo para hallar integrales
import numpy as np
import matplotlib.pyplot as plt

go = True
try:
    f = str(input("Ingrese una funcion (use 'x' como variable dependiente): ")) # np.arcsin(x)
    a = float(input("Ingrese un numero real (Limite inferior): "))          # 0.5
    b = float(input("Ingrese un numero real (Limite superior): "))          # 1
    n = int(input("Ingrese un numero natural (Numero de divisiones): "))       # 4
    if (a > b) or (n < 1):
        print('Invalid range or number of chunks')
        go = False
except:
    print('Invalid Data')
    go = False
if go:
    h = (b-a)/n

    suma = 0

    def evaluar_funcion(x):
        return eval(f)

    x = np.linspace(a,b,n+1)

    for i in range(1, n):
        x_value = a + h*i
        if(i % 2 == 0):
            suma += 2 * evaluar_funcion(x_value)
        else:
            suma += 4 * evaluar_funcion(x_value)
    suma += (evaluar_funcion(a) + evaluar_funcion(b))
    f_int = suma*(h/3)

    print("El resultado de la integral es:", f_int)

    plt.plot(x,evaluar_funcion(x))
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title("Funcion")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.show()