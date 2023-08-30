import math

a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

if ((a+b)>=c and (a+c)>=b and (b+c)>=a):
    s = (a+b+c)/2
    area = math.sqrt(s+(s-a)*(s-b)*(s-c))
    print(area)
    if (a==b==c):
        print("Equilatero")
    elif (a==b) and ((a!=c)or(b!=c)):
        print("Isosceles")
    elif (a!=b!=c):
        print("Escaleno")
else:
    print("No forma un triángulo")
