# Resolucion 1

N = int(input("Ingrese el numero de personas: "))
alturas = []

for i in range(N):
    altura = float(input(f"Ingrese la altura de la persona {i+1}: "))
    alturas.append(altura)

media = sum(alturas) / N
mayores = sum(1 for altura in alturas if altura > media)
menores = sum(1 for altura in alturas if altura < media)

print("Altura media:", media)
print("Personas con altura superior a la media:", mayores)
print("Personas con altura inferior a la media:", menores)

#Resolucion 2

numeros = list(map(int, input("Ingrese 10 numeros enteros separados por espacio: ").split()))

positivos = [num for num in numeros if num > 0]
negativos = [num for num in numeros if num < 0]

mediapositivos = sum(positivos) / len(positivos) if positivos else "No hay valores positivos en el array."
medianegativos = sum(negativos) / len(negativos) if negativos else "No hay valores negativos en el array."

print("Media de los valores positivos:", mediapositivos)
print("Media de los valores negativos:", medianegativos)


#Resolucion 3

numeros = list(map(int, input("Ingrese 10 numeros enteros separados por espacio: ").split()))

positivos = sum(1 for num in numeros if num > 0)
negativos = sum(1 for num in numeros if num < 0)
ceros = sum(1 for num in numeros if num == 0)

print("Cantidad de numeros positivos:", positivos)
print("Cantidad de numeros negativos:", negativos)
print("Cantidad de ceros:", ceros)


#Resolucion 4

def numeroAlumnos():
    N = int(input("Ingrese el numero de alumnos de la clase: "))
    return N

def leerAlturas(N):
    alturas = []
    for i in range(N):
        altura = float(input(f"Ingrese la altura del alumno {i+1}: "))
        alturas.append(altura)
    return alturas

def calcularMedias(alturas):
    return sum(alturas) / len(alturas)

def mostrarResultados(alturas, media):
    mayores = sum(1 for altura in alturas if altura > media)
    menores = sum(1 for altura in alturas if altura < media)
    print("Altura media de los alumnos:", media)
    print("Cantidad de alumnos mas altos que la media:", mayores)
    print("Cantidad de alumnos mas bajos que la media:", menores)

N = numeroAlumnos()
alturas = leerAlturas(N)
media = calcularMedias(alturas)
mostrarResultados(alturas, media)
