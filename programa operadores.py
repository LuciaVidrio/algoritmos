x = 22 #aqui se asigna el valor 22 a la variable x y será en binario
print ("x = {: >6b}". format ( x ) )# Imprime el valor binario de x alineado a la derecha con un ancho de 6 caracteres
print ("x & 4 = {: >3d} = {: >6b}". format ( x & 4 , x & 4) )# Realiza la operación bit a bit AND entre x y 4, luego imprime el resultado en decimal y binario
print ("x | 1 = {: >3d} = {: >6b}". format ( x | 1 , x | 1) )# Realiza la operación bit a bit OR entre x y 1, luego imprime el resultado en decimal y binario
print ("x ^ 4 = {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )# Realiza la operación bit a bit XOR entre x y 4, luego imprime el resultado en decimal y binario
print ("~x = {: >3d} = {: >6b}". format (~ x , ~ x ) )# Realiza la operación bit a bit NOT (complemento de uno) en x, luego imprime el resultado en decimal y binario
print ("x << 1 = {: >3d} = {: >6b}". format ( x << 1 , x << 1) )# Desplaza los bits de x hacia la izquierda en una posición, luego imprime el resultado en decimal y binario
print ("x >> 2 = {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )# Desplaza los bits de x hacia la derecha en dos posiciones, luego imprime el resultado en decimal y binario
