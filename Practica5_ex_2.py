Ci = float(input("Cantidad a invertir: "))
i = float(input("Interes anual: "))
n = int(input("Numero de anios: "))

for j in range(1, n+1):
    Cf = Ci*((1+(i/100))**n)
print("Capital obtenido en la inversión cada año que dura la inversión:", Cf)