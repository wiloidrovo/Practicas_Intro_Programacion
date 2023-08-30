nombre = str(input("Ingrese su nombre: "))
sexo = str(input("Ingrese su sexo (masculino/femenino): "))

match sexo:
    case "femenino":
        if (nombre[0].lower() in ["a", "b", "c", "d", "e", "f",
                                  "g", "h", "i", "j", "k", "l"]):
            print("Grupo A")
        else:
            print("Grupo B")
    case "masculino":
        if nombre[0].lower() in ["o","p","q","r","s","t",
                                 "u","v","w","x","y","z"]:
            print("Grupo A")
        else:
            print("Grupo B")
