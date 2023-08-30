# Método de Bisección para hallar la raíz de una función
import numpy as np
f = str(input("Ingrese una funcion f(x): "))
def evaluar_funcion(x):
    return eval(f)
go = True
while(go):
    a = float(input("Ingrese un numero real: "))
    b = float(input("Ingrese un numero real mayor que el anterior: "))
    if (a < b) and ((evaluar_funcion(a) * evaluar_funcion(b)) < 0):
        go = False
error = 0.0000001
c = (a+b)/2
c_anterior = a
while(evaluar_funcion(c) != 0) and (abs(c - c_anterior) > error):
    if((evaluar_funcion(c) * evaluar_funcion(b)) < 0):
        a = c
    else:
        b = c
    c_anterior = c
    c = (a+b)/2
print("La funcion", f, "tiene una raiz en x =", c)