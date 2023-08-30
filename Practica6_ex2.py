# Método de la Secante para hallar la raíz de una función
import sympy as sp

x = sp.Symbol("x")
f = sp.sympify(input("Ingrese una funcion f(x): "))
f_num = sp.lambdify(x, f)
go = True
while go:
    x0 = float(input("Ingrese x0: "))
    x1 = float(input("Ingrese x1: "))
    if (f_num(x0)!=f_num(x1)):
        go = False

tolerancia = 0.0000001
error = 1
print("Aproximaciones:")
contador = 0
while(error >= tolerancia):
    x2 = x1 - ((x1-x0)/(f_num(x1)-f_num(x0)))*f_num(x1)
    x0 = x1
    x1 = x2
    error = abs(f_num(x2))
    contador+=1
    subindice = chr(8320 + contador)
    print("x"+ subindice+ "=", x1)
if error < tolerancia:
    print("La raiz de (" + str(f) + ") es =", x1)