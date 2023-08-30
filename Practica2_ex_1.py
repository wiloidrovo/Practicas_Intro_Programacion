passw = str(input("Ingrese su contraseña: "))
new_passw = str(input("Verifique su contraseña: "))

if (new_passw.lower() == passw.lower()):
    print("Contraseña correcta")
else:
    print("Error")