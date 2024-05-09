/*1.	Programa C++ que lea el nombre y el sueldo de 6 empleados y 
muestre el nombre y el sueldo del empleado que más gana. 
Para hacerlo utilizaremos dos arrays: 

Un array de String para los nombres de los empleados 
Un array de tipo double para los sueldos de cada empleado. 

Al mismo tiempo que leemos los datos de los empleados iremos comprobando cuál es el que tiene el mayor sueldo.
Para ello tomamos el sueldo del primer empleado que se lee como mayor sueldo y después vamos comprobando el resto de sueldos.

Cuando encontramos alguno mayor que el mayor actual este sueldo se convierte en el nuevo mayor.
Finalmente mostrar el salario neto de la suma de los sueldos, e indicar a quien pertenece el salario mayor. */


CODIGO

/*Universidad Salesia de Bolivia
Carrera: Ingenieria de sistema
programacion 1
Bernardo Vargas Ruiz*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    string nombres[6];
    double sueldos[6];
    double msueldo = 0;
    int mayors = 0;
    for (int i = 0; i < 6; ++i) {
        cout << "Ingrese el nombre del empleado "<< i+1 << ": ";
        cin >> nombres[i];
        cout << "Ingrese el sueldo de " << nombres[i] << ": ";
        cin >> sueldos[i];
        
        if (sueldos[i] > msueldo) {
            msueldo = sueldos[i];
            mayors = i;
        }
    }
    cout << "El empleado con el mayor sueldo es: " << nombres[mayors] << endl;
    cout << "Su sueldo es: " << sueldos[mayors] << endl;

    double sumasueldos = 0;
    for (int i = 0; i < 6; ++i) {
        sumasueldos += sueldos[i];
    }
    cout << "La suma de los sueldos es: " << sumasueldos << endl; 

    return 0;
}
