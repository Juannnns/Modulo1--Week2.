
# Determinar estado de aprobación 
while True:
    calificacion = input("Ingrese su calificación: ")
    if calificacion.isdigit():
        calificacion = int(calificacion)
        if 0 <= calificacion <= 100:
            if calificacion >=60:
                print("El estudiante ha aprobado")
            else:
                ("El estudiante ha reprobado")
            break
        else:
            ("La calificación de estar entre 0 y 100")
    else:
        print("Entrada no válida. Ingrese un valor válido")

# Calcula el promedio de una lista de calificaciones 

while True:
    notas = input("Ingrese varias de sus calificaciones separadas por comas: ")
    lista_str = notas.split(",")
    calificaciones = []
    for item in lista_str:
        item = item.strip()
        if item.isdigit():
            num = int(item)
            if 0 <= num <= 100:
                calificaciones.append(num)
            else:
                print(f"Ignorando valor fuera del rango: {item}")
        else:
            print(f"Entrada no válida: {item}")
    if len(calificaciones) > 0:
        suma = 0
        for nota in calificaciones:
            suma += nota
        promedio = suma / len(calificaciones)
        print(f"El promedio es de: {promedio:.2f}")
        break
    else:
        print("No se ingresaron notas validas")
        
# Contar calificaciones mayores 
while True:
    valor = input("Ingrese un valor para contar cuántas calificaciones son mayores que este: ")
    if valor.isdigit():
        valor = int(valor)
        contador = 0
        for nota in calificaciones:
            if nota > valor:
                contador += 1
        print(f"Hay {contador} calificaciones mayor que {valor}")
        break
    else:
        print("Por favor ingrese un valor válido")
    
# Verificar y contar calificaciones especifica
while True:
    buscar = input("Ingrese una calificación para verificar cuántas veces aparece: ")
    if buscar.isdigit():
        buscar = int(buscar)
        conteo = 0 
        for nota in calificaciones:
            if nota < 0 or nota > 100:
                continue          # Ignorar datos iválidos si los hubiera
            if nota == buscar:
                conteo += 1        
        print(f"La calificación {buscar} sale {conteo} veces ")
        break              # Salir del while después de una entrada válida y mostara los resultados
    else:
        print("Entrada no válida. Ingresa un valor correcto")