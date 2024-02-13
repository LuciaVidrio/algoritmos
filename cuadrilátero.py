def identificar_cuadrilatero(lados):
    lados_ordenados = sorted(lados)  # ordenar los lados de menor a mayor
    if lados_ordenados[0] == lados_ordenados[1] == lados_ordenados[2] == lados_ordenados[3]:  # si es cuadrado
        return "Cuadrado"
    elif lados_ordenados[0] == lados_ordenados[1] and lados_ordenados[2] == lados_ordenados[3]:
        return "Rectángulo"
    else:
        return "Otro Cuadrilátero"

# lados de las medidas del usuario
lados = []
for i in range(4):
    lado = float(input(f"Ingrese la medida del lado {i + 1}: "))
    lados.append(lado)

# define el tipo de cuadrilátero
tipo_cuadrilatero = identificar_cuadrilatero(lados)

# muestra el resultado
print(f"El cuadrilátero es: {tipo_cuadrilatero}")
