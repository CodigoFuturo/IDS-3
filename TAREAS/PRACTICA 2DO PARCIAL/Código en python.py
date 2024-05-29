====================================================================================================
====================================================================================================
EJERCICIO 1

def calcular_promedio(calificaciones):
    for i in range(len(calificaciones)):
        suma = sum(calificaciones[i])
        promedio = suma / len(calificaciones[i])
        print(f"El promedio de calificaciones del estudiante {i+1} es: {promedio}")

def ordenar_calificaciones(calificaciones):
    for i in range(len(calificaciones)):
        calificaciones[i] = sorted(calificaciones[i], reverse=True)

def encontrar_maxima_calificacion(calificaciones, asignatura):
    maxima_calificacion = max(estudiante[asignatura] for estudiante in calificaciones)
    return maxima_calificacion

def main():
    num_estudiantes = 3
    calificaciones = []

    print("Ingrese las calificaciones de los estudiantes:")
    for i in range(num_estudiantes):
        estudiante = []
        print(f"Estudiante {i + 1}:")
        for j in range(5):
            calificacion = int(input(f"Ingrese la calificación {j + 1}: "))
            estudiante.append(calificacion)
        calificaciones.append(estudiante)

    calcular_promedio(calificaciones)
    ordenar_calificaciones(calificaciones)

    print("Calificaciones ordenadas de cada estudiante:")
    for i in range(num_estudiantes):
        print(f"Estudiante {i + 1}: {calificaciones[i]}")

    asignatura = int(input("Ingrese el número de la asignatura (0-4): "))

    maxima_calificacion = encontrar_maxima_calificacion(calificaciones, asignatura)
    print(f"La calificación más alta en la asignatura {asignatura} es: {maxima_calificacion}")

if __name__ == "__main__":
    main()


====================================================================================================
====================================================================================================
EJERCICIO 2

MAX_PRODUCTOS = 100
inventario = []
num_productos = 0

def agregar_producto():
    global num_productos
    if num_productos < MAX_PRODUCTOS:
        codigo = int(input("Ingrese el código del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad en stock: "))
        
        inventario.append({"codigo": codigo, "nombre": nombre, "cantidad": cantidad})
        num_productos += 1
        print("Producto agregado al inventario.")
    else:
        print("No se puede agregar más productos, inventario lleno.")

def ordenar_inventario():
    global inventario
    inventario = sorted(inventario, key=lambda x: x["nombre"])
    print("Inventario ordenado por nombre del producto.")

def buscar_producto_por_codigo():
    codigo = int(input("Ingrese el código del producto: "))
    encontrado = False
    for producto in inventario:
        if producto["codigo"] == codigo:
            print("Producto encontrado:")
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad en stock: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado en el inventario.")

def vender_producto():
    codigo = int(input("Ingrese el código del producto: "))
    for producto in inventario:
        if producto["codigo"] == codigo:
            cantidad = int(input("Ingrese la cantidad a vender: "))
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                print("Venta realizada. Stock actualizado.")
            else:
                print("No hay suficiente stock para realizar la venta.")
            return
    print("Producto no encontrado en el inventario.")

def recibir_stock():
    codigo = int(input("Ingrese el código del producto: "))
    for producto in inventario:
        if producto["codigo"] == codigo:
            cantidad = int(input("Ingrese la cantidad a recibir: "))
            producto["cantidad"] += cantidad
            print("Stock actualizado.")
            return
    print("Producto no encontrado en el inventario.")

def main():
    while True:
        print("MENU DE OPCIONES")
        print("1. Agregar producto")
        print("2. Ordenar inventario")
        print("3. Buscar producto por código")
        print("4. Vender producto")
        print("5. Recibir stock")
        print("6. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ordenar_inventario()
        elif opcion == '3':
            buscar_producto_por_codigo()
        elif opcion == '4':
            vender_producto()
        elif opcion == '5':
            recibir_stock()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()





====================================================================================================
====================================================================================================
EJERCICIO 3

FILAS = 5
COLUMNAS = 5
tablero = [[0] * COLUMNAS for _ in range(FILAS)]

def inicializar_tablero():
    global tablero
    for i in range(FILAS):
        for j in range(COLUMNAS):
            tablero[i][j] = 0

def colocar_ficha(fila, columna, tipo_ficha):
    global tablero
    tablero[fila][columna] = tipo_ficha

def buscar_linea(fila, columna, tipo_ficha):
    return False

def imprimir_tablero():
    for fila in tablero:
        print(" ".join(map(str, fila)))

def main():
    inicializar_tablero()
    tipo_ficha = 1
    for turno in range(1, FILAS * COLUMNAS + 1):
        print(f"Turno del Jugador {tipo_ficha}")
        imprimir_tablero()
        fila = int(input("Jugador {}, elige una fila: ".format(tipo_ficha))) - 1
        columna = int(input("Jugador {}, elige una columna: ".format(tipo_ficha))) - 1
        if 0 <= fila < FILAS and 0 <= columna < COLUMNAS and tablero[fila][columna] == 0:
            colocar_ficha(fila, columna, tipo_ficha)
            if buscar_linea(fila, columna, tipo_ficha):
                print("¡Felicidades! Jugador {} ha ganado.".format(tipo_ficha))
                break
            tipo_ficha = 2 if tipo_ficha == 1 else 1
        else:
            print("Fila y/o columna inválida. Por favor, elige otra casilla.")

    else:
        print("¡El juego ha terminado en empate!")
    print("Estado final del tablero:")
    imprimir_tablero()

if __name__ == "__main__":
    main()

====================================================================================================
====================================================================================================
EJERCICIO 4

DIAS = 3
HORAS = 4

def temperatura_promedio_diaria(temperaturas):
    for dia, temperatura_dia in enumerate(temperaturas, start=1):
        promedio = sum(temperatura_dia) / len(temperatura_dia)
        print(f"Temperatura promedio del día {dia}: {promedio}°C")

def ordenar_temperaturas(temperaturas):
    for dia, temperatura_dia in enumerate(temperaturas):
        temperaturas[dia] = sorted(temperatura_dia)

def encontrar_extremos(temperaturas):
    temperaturas_planas = [temperatura for temperatura_dia in temperaturas for temperatura in temperatura_dia]
    maxima = max(temperaturas_planas)
    minima = min(temperaturas_planas)
    dia_maxima = temperaturas_planas.index(maxima) // HORAS + 1
    dia_minima = temperaturas_planas.index(minima) // HORAS + 1
    print(f"Día con la temperatura más alta: {dia_maxima} (Temperatura: {maxima}°C)")
    print(f"Día con la temperatura más baja: {dia_minima} (Temperatura: {minima}°C)")

def main():
    temperaturas = []
    print("Ingrese las temperaturas diarias para {} días y {} horas por día:".format(DIAS, HORAS))
    for dia in range(DIAS):
        temperatura_dia = []
        print("Día {}:".format(dia + 1))
        for hora in range(HORAS):
            temperatura = float(input("Temperatura para la hora {}: ".format(hora + 1)))
            temperatura_dia.append(temperatura)
        temperaturas.append(temperatura_dia)

    temperatura_promedio_diaria(temperaturas)
    ordenar_temperaturas(temperaturas)
    encontrar_extremos(temperaturas)

if __name__ == "__main__":
    main()

====================================================================================================
====================================================================================================
EJERCICIO 5

MAX_CIUDADES = 9

def ingresar_distancias(distancias):
    num_ciudades = len(distancias)
    print("Ingrese las distancias entre las ciudades:")
    for i in range(num_ciudades):
        for j in range(num_ciudades):
            distancias[i][j] = int(input(f"Distancia de la ciudad {i + 1} a la ciudad {j + 1}: "))

def suma_distancias_ciudad(distancias, ciudad):
    return sum(distancias[ciudad])

def comparar_distancias_totales(ciudad1, ciudad2, distancias):
    return suma_distancias_ciudad(distancias, ciudad1) < suma_distancias_ciudad(distancias, ciudad2)

def ordenar_ciudades_por_distancia_total(distancias):
    ciudades = [(ciudad, suma_distancias_ciudad(distancias, ciudad)) for ciudad in range(len(distancias))]
    ciudades.sort(key=lambda x: x[1])
    print("Ciudades ordenadas por su distancia total a todas las demás:")
    for ciudad, distancia_total in ciudades:
        print(f"Ciudad {ciudad + 1}: Distancia total = {distancia_total}")

def distancia_minima_entre_ciudades(distancias, ciudad1, ciudad2):
    return distancias[ciudad1][ciudad2]

def imprimir_matriz_distancias(distancias):
    print("Matriz de distancias entre ciudades:")
    for fila in distancias:
        print(" ".join(map(str, fila)))

def main():
    num_ciudades = int(input(f"Ingrese el número de ciudades (máximo {MAX_CIUDADES}): "))
    if num_ciudades < 2 or num_ciudades > MAX_CIUDADES:
        print("Número de ciudades no válido.")
        return

    distancias = [[0] * num_ciudades for _ in range(num_ciudades)]

    ingresar_distancias(distancias)

    imprimir_matriz_distancias(distancias)

    ordenar_ciudades_por_distancia_total(distancias)

    ciudad1 = int(input(f"Ingrese el número de la primera ciudad (1-{num_ciudades}): ")) - 1
    ciudad2 = int(input(f"Ingrese el número de la segunda ciudad (1-{num_ciudades}): ")) - 1
    if not (0 <= ciudad1 < num_ciudades and 0 <= ciudad2 < num_ciudades):
        print("Números de ciudades no válidos.")
        return

    print(f"La distancia mínima entre la Ciudad {ciudad1 + 1} y la Ciudad {ciudad2 + 1} es: {distancia_minima_entre_ciudades(distancias, ciudad1, ciudad2)}")

if __name__ == "__main__":
    main()

====================================================================================================
====================================================================================================
EJERCICIO 6

ESTUDIANTES = 5
MATERIAS = 3

def ingresar_notas(notas):
    print(f"Ingrese las notas de los estudiantes para {MATERIAS} materias y {ESTUDIANTES} estudiantes:")
    for i in range(ESTUDIANTES):
        print(f"Estudiante {i + 1}:")
        for j in range(MATERIAS):
            notas[i][j] = int(input(f"Nota para la materia {j + 1}: "))

def calcular_promedios(notas):
    for i in range(ESTUDIANTES):
        promedio = sum(notas[i]) / MATERIAS
        print(f"El promedio de notas del Estudiante {i + 1} es: {promedio:.2f}")

def ordenar_notas(notas):
    for i in range(ESTUDIANTES):
        notas[i].sort(reverse=True)

def encontrar_nota_maxima(notas, materia):
    return max(estudiante[materia] for estudiante in notas)

def encontrar_nota_minima(notas, materia):
    return min(estudiante[materia] for estudiante in notas)

def imprimir_datos(notas, materia):
    print("Notas de los estudiantes:")
    for i, estudiante in enumerate(notas, start=1):
        print(f"Estudiante {i}: {', '.join(map(str, estudiante))}")

    print("\nPromedios de notas:")
    calcular_promedios(notas)

    print("\nNotas más alta y más baja en la materia {}:".format(materia + 1))
    print(f"Nota más alta: {encontrar_nota_maxima(notas, materia)}")
    print(f"Nota más baja: {encontrar_nota_minima(notas, materia)}")

def main():
    notas = [[0] * MATERIAS for _ in range(ESTUDIANTES)]

    ingresar_notas(notas)

    ordenar_notas(notas)

    materia = int(input(f"Ingrese el número de la materia para encontrar las notas más alta y más baja (1-{MATERIAS}): ")) - 1
    if not (0 <= materia < MATERIAS):
        print("Número de materia no válido.")
        return

    imprimir_datos(notas, materia)

if __name__ == "__main__":
    main()

