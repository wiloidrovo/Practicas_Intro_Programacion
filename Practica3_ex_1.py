par_1 = complex(input("Ingrese el primer numero complejo: "))
par_2 = complex(input("Ingrese el segundo numero complejo: "))
operador = str(input("Ingrese un operador: "))

if (operador == "+"):
    print (par_1+par_2)
elif (operador == "-"):
    print (par_1-par_2)
elif (operador == "*"):
    print (par_1*par_2)
elif (operador == "/"):
    print (par_1/par_2)
else: 
    print("Operación no soportada")