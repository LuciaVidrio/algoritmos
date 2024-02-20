UNIDAD = (
    '', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'
)

TEENS = (
    'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete',
    'dieciocho', 'diecinueve'
)

DECENAS = (
    'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'
)

CENTENAS = (
    'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos',
    'setecientos', 'ochocientos', 'novecientos'
)
#funcion o metodo convertir letras
def convertir_a_letras(numero):
    if numero < 10:
        return UNIDAD[numero]
    elif numero < 20:
        return TEENS[numero - 10]
    elif numero < 100:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return DECENAS[decena - 2]
        else:
            return DECENAS[decena - 2] + ' y ' + UNIDAD[unidad]
    elif numero < 1000:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            if centena == 1:
                return CENTENAS[0]
            else:
                return CENTENAS[centena - 1]
        else:
            return CENTENAS[centena - 1] + ' ' + convertir_a_letras(resto)
    elif numero < 1000000:
        millar = numero // 1000
        resto = numero % 1000
        if millar == 1:
            return 'mil ' + convertir_a_letras(resto)
        else:
            return convertir_a_letras(millar) + ' mil ' + convertir_a_letras(resto)
    elif numero < 1000000000:
        millon = numero // 1000000
        resto = numero % 1000000
        if millon == 1:
            return 'un millón ' + convertir_a_letras(resto)
        else:
            return convertir_a_letras(millon) + ' millones ' + convertir_a_letras(resto)
    elif numero < 1000000000000:
        billon = numero // 1000000000
        resto = numero % 1000000000
        if billon == 1:
            return 'mil millones ' + convertir_a_letras(resto)
        else:
            return convertir_a_letras(billon) + ' mil millones ' + convertir_a_letras(resto)
    elif numero < 1000000000000000:
        trillon = numero // 1000000000000
        resto = numero % 1000000000000
        if trillon == 1:
            return 'un trillón ' + convertir_a_letras(resto)
        else:
            return convertir_a_letras(trillon) + ' trillones ' + convertir_a_letras(resto)

continuar = True

# Bucle
while continuar:
   
    numero = int(input('Ingresa un número: '))
    
    # Convertir el número a letras
    print(convertir_a_letras(numero))
  
    opcion = input("1. Continuar\n2. Finalizar\n")
    
  
    if opcion == "1":
        print("Continuando...")
    elif opcion == "2":
        print("Adios popó...")
        continuar = False
    else:
        print("Opción inválida, por favor ingresa 1 o 2.")
        

print("programa finalizado...")