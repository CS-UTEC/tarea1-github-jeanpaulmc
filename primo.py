number = int(input("Ingrese un numero:"))
cont = 1
if ( number <= 1):
    print( "El numero No es primo.")
else: 
    for i in range(2, number):
        if (number % i == 0):
                cont = cont + 1
    if (cont > 1):
        print("El numero NO es primo")
    else:
        print("El numero SI es primo")
