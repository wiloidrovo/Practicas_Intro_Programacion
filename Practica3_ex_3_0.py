n = int(input("Ingrese el numero de datos: "))
array = []
for i in range(n):
    value = int(input("Ingrese un numero real: "))
    array.append(value)
print(sorted(array))