fecha = str(input("Ingrese una fecha valida (DD/MM/AAAA): "))
date = fecha.split("/")
date = [int(i) for i in date]

maximo=False
match (date[1]):
    case 1 | 3 | 5 | 7 | 8 | 10:
        day_max = 31
    case 2:
        if ((date[2]%4)==0 and (date[2]%100)!=0 or (date[2]%400)==0):
            print("El año",date[2],"es un año bisiesto")
            day_max = 29
        else:
            day_max = 28
    case 12:
        day_max = 31
        maximo = True
        if (date[0]==31):
            date[0] = 1
            date[1] = 1
            date[2] += 1
        else:
            date[0] += 1
    case _:
        day_max = 30

if (maximo == False):
    if (date[0]==day_max):
        date[0] = 1
        date[1] += 1
    else:
        date[0] += 1
print("El dia siguiente es: ", date[0],"/", date[1], "/", date[2])