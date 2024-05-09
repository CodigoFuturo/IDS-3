"""
1.	Programa C++ que lea el nombre y el sueldo de 6 empleados y 
muestre el nombre y el sueldo del empleado que más gana. 
Para hacerlo utilizaremos dos arrays: 

Un array de String para los nombres de los empleados 
Un array de tipo double para los sueldos de cada empleado. 

Al mismo tiempo que leemos los datos de los empleados iremos comprobando cuál es el que tiene el mayor sueldo.
Para ello tomamos el sueldo del primer empleado que se lee como mayor sueldo y después vamos comprobando el resto de sueldos.

Cuando encontramos alguno mayor que el mayor actual este sueldo se convierte en el nuevo mayor.
Finalmente mostrar el salario neto de la suma de los sueldos, e indicar a quien pertenece el salario mayor.
"""

# CODIGO
"""
 Universidad Salesia de Bolivia
 Carrera: Ingenieria de sistema
 Programacion 1
 Bernardo Vargas Ruiz
"""
nombres = []
sueldos = []
mayor_sueldo = 0
indice_mayor_sueldo = 0

for i in range(6):
    nombre = input("Ingrese el nombre del empleado " + str(i+1) + ": ")
    nombres.append(nombre)
    sueldo = float(input("Ingrese el sueldo de " + nombre + ": "))
    sueldos.append(sueldo)

    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        indice_mayor_sueldo = i

print("El empleado con el mayor sueldo es:", nombres[indice_mayor_sueldo])
print("Su sueldo es:", sueldos[indice_mayor_sueldo])

suma_sueldos = sum(sueldos)
print("La suma de los sueldos es:", suma_sueldos)
