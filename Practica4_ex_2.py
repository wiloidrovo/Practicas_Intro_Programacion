x = int(input("Ingrese un numero entero de tres cifras: "))

centenas = x//100
decenas = x//10
unidades = x%10
conector = " y "

match x:
    case 0:
        centenas = " "
        decenas = "cero"
        conector = " "
        unidades = " "
    case 11:
        centenas = " "
        decenas = "once"
        conector = " "
        unidades = " "
    case 12:
        centenas = " "
        decenas = "doce"
        conector = " "
        unidades = " "
    case 13:
        centenas = " "
        decenas = "trece"
        conector = " "
        unidades = " "
    case 14:
        centenas = " "
        decenas = "catorce"
        conector = " "
        unidades = " "
    case 15:
        centenas = " "
        decenas = "quince"
        conector = " "
        unidades = " "
    case 100:
        centenas = "cien"
        decenas = " "
        conector = " "
        unidades = " "
    case _:
        cent = x//100
        if cent != 0:
            dec_pre = x%100
            dec = dec_pre//10
        else:
            dec = x // 10
        uni = x % 10
        conector = "y"
        match cent:
            case 0:
               centenas = " "
            case 1:
                centenas = "ciento"
            case 2:
                centenas = "doscientos"
            case 3:
                centenas = "trescientos"
            case 4:
                centenas = "cuatrocientos"
            case 5:
                centenas = "quinientos"
            case 6:
                centenas = "seiscientos"
            case 7:
                centenas = "setecientos"
            case 8:
                centenas = "ochocientos"
            case 9:
                centenas = "novecientos"
        match dec:
            case 0:
                conector = " "
                decenas = " "
            case 1:
                decenas = "diez"
            case 2:
                decenas = "veinte"
            case 3:
                decenas = "treinta"
            case 4:
                decenas = "cuarenta"
            case 5:
                decenas = "cincuenta"
            case 6:
                decenas = "sesenta"
            case 7:
                decenas = "setenta"
            case 8:
                decenas = "ochenta"
            case 9:
                decenas = "noventa"
        match uni:
            case 0:
                conector = " "
                unidades = " "
            case 1:
                unidades = "uno"
            case 2:
                unidades = "dos"
            case 3:
                unidades = "tres"
            case 4:
                unidades = "cuatro"
            case 5:
                unidades = "cinco"
            case 6:
                unidades = "seis"
            case 7:
                unidades = "siete"
            case 8:
                unidades = "ocho"
            case 9:
                unidades = "nueve"
                
print(centenas, decenas, conector, unidades)