n = int(input("Ingrese un número natural: "))

for i in range(2, n):
    num_div = 0
    #print("i: ",i)
    for j in range(1, i + 1):
        #print("j: ",j)
        if i % j == 0:
            num_div += 1
    if num_div == 2:
        print(i)