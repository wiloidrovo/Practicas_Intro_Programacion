x = str(input("Ingrese cualquier numero o letra (solo 1): ")).lower()

match len(x):
    case 1:
        match x:
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                print("Es un digito")
            case "a" | "e"| "i" | "o" | "u":
                print("Es una vocal")
            case _:
                print("Es una consonante")
    case _:
        print("La cantidad de caracteres ingresados es mayor a 1")