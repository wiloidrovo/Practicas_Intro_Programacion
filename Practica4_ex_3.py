x = str(input("Ingrese color 1: ")).lower()
y = str(input("Ingrese color 2: ")).lower()

if x not in ['azul', 'rojo', 'verde'] or y not in ['azul', 'rojo', 'verde']:
    print("Error") 
else:
    if (x!="rojo"):
        temp = y
        y=x
        x=temp

    if (x == "azul") and (y == "verde"):
        x = "verde"
        y = "azul"

    match x:
        case "rojo":
            if (y == "azul"):
                print("morado")
            elif (y == "verde"):
                print("amarillo")
        case "verde":
            if (y == "azul"):
                print("turquesa")