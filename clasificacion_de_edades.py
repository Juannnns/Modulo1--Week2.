# Solicita la edad al usuario
edad = int(input("Ingrese su edad: "))

# Clasificar según su rango de edad usando condicionales
if edad <18:
    print(f"Su edad es {edad} por lo tanto es menor de edad")
elif edad <=30:
    # Aqui ya sabemos que edad >= 18 por la condición anterior
    print(f"Su edad es {edad} por lo tanto es un adulto joven")
elif edad <=65:
    # Aqui ya sabemos que edad > 30 por la condición anterior
    print(f"Su edad es {edad} por lo tanto es un adulto maduro")
else:
    #Si no se cumle ninguna de las anteriores, entonces edad > 65
    print(f"Su edad es {edad} por lo tanto es un adulto mayor")

