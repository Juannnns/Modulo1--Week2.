# Solicita un número al usuario
numero = int(input("Ingrese su número entero: "))

# Determina si el número es positivo, negativo o cero
if numero >0:
    print("El numero es positivo")
elif numero <0:
    print("El numero es negativo")
else:
    print("El numero es cero")

# Solo si el número no es cero, determina si es par o impar 
if numero !=0:
    if numero % 2 == 0:
        # El operador % calcula el residuo de la división  entre el número y 2
        print("Además, el número es par")
else:
    print("Además, el numero es impar")
    