print("Bienvenid@ al Cálculo de la Constante de Conway")
numero = input("Por favor, introduce un número para iniciar la secuencia: ")
iteraciones = input("Por favor, introduce el número de iteraciones: ")


iteraciones = int(iteraciones)  # Será el número de veces que queramos calcular el siguiente numero dentro de esta secuencia
primeraVez = True
vueltas = 0
numeroNuevo = ""    # Contendrá el siguiente número de la serie (en realidad es un string de dígitos)

print (numero)

while vueltas < iteraciones:
    indice = 1

    if primeraVez:
        primeraVez = False
    else:
        numero = numeroNuevo    # Una vez parseado el numero y averiguado el siguiente de la serie hacemos que el numero sea el nuevoNumero
        numeroNuevo = ""        # A continuación hacemos que nuevoNumero esté vacio

    caracAnterior = numero[0]
    contador = 0

    for x in numero:
        longitud = len(numero)

        if x == caracAnterior and indice == longitud:
            contador += 1
            numeroNuevo = numeroNuevo + str(contador) + x
            contador = 0
        elif x != caracAnterior and indice == longitud:
            numeroNuevo = numeroNuevo + str(contador) + caracAnterior + "1" + x
            contador = 0
        elif x == caracAnterior:
            contador += 1
        elif x != caracAnterior and indice != longitud:
            numeroNuevo = numeroNuevo + str(contador) + caracAnterior
            caracAnterior = x
            contador = 1
        else:
            numeroNuevo = numeroNuevo + str(contador) + x
            contador = 0
            caracAnterior = x
        indice += 1
    print (numeroNuevo)

    vueltas +=1