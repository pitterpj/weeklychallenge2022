#  00 weeklychallenge2022

#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

list_fizz_buzz = [i for i in range(1,101)]
for num in list_fizz_buzz:
    if(num % 3 == 0) and (num % 5 == 0):
        print("fizzbuzzy")
    elif(num % 3 == 0):
        print("fizz")
    elif(num % 5 == 0):
        print("buzz")
    else:
        print(num)
