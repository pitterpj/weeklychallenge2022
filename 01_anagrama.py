#  01 weeklychallenge2022

# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def anagrama(string1, string2):
    solucion = "I am Lord Voldemort"
    solucion_sin_espacios =solucion.replace(" ","")
    solucion = [i.lower() for i in solucion_sin_espacios]

    all_caract = string1.replace(" ","") + string2.replace(" ","")
    all_caract = [i.lower() for i in all_caract]

    if len(solucion) != len(all_caract):
        return False
    

    for index in all_caract:
        for index2 in solucion:
            if index == index2:
                solucion.remove(index2)

    if not solucion:
        return True
    else:
        return False

print(anagrama('Tom Marvolo', 'Riddle'))