# Replace the "ANSWER HERE" for your answer

def power(base, exp):

    resultado = 1
    for number in range(exp):
        resultado=resultado*base
    return resultado


def sum_of_powers(base, max_exp):
    suma = 0
    for number in range(max_exp + 1):
        suma=suma + power(base,number)
    return suma

