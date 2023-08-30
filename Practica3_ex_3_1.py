n1 = float(input("numero 1: "))
n2 = float(input("numero 2: "))
n3 = float(input("numero 3: "))

if n1>n2 and n2>n3:
    print("orden:", n3, n2, n1)
elif n2>n1 and n1>n3:
    print("orden:", n3, n1, n2)
elif n1>n3 and n3>n2:
    print("orden:", n2, n3, n1)
elif n3>n1 and n1>n2:
    print("orden:", n2, n1, n3)
elif n2>n3 and n3>n1:
    print("orden:", n1, n3, n2)
else:
    print("orden:", n1, n2, n3)