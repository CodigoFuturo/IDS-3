EJERCICIO 1
  #include <iostream>
#include <algorithm>

using namespace std;

void calcularPromedio(int calificaciones[][5], int numEstudiantes) {
    for (int i = 0; i < numEstudiantes; ++i) {
        double suma = 0;
        for (int j = 0; j < 5; ++j) {
            suma += calificaciones[i][j];
        }
        double promedio = suma / 5;
        cout << "El promedio de calificaciones del estudiante " << i+1 << " es: " << promedio << endl;
    }
}

void ordenarCalificaciones(int calificaciones[][5], int numEstudiantes) {
    for (int i = 0; i < numEstudiantes; ++i) {
        sort(calificaciones[i], calificaciones[i] + 5, greater<int>());
    }
}

int encontrarMaximaCalificacion(int calificaciones[][5], int numEstudiantes, int asignatura) {
    int maximaCalificacion = calificaciones[0][asignatura];
    for (int i = 1; i < numEstudiantes; ++i) {
        maximaCalificacion = max(maximaCalificacion, calificaciones[i][asignatura]);
    }
    return maximaCalificacion;
}

int main() {
    const int numEstudiantes = 3;
    int calificaciones[numEstudiantes][5];

    cout << "Ingrese las calificaciones de los estudiantes:" << endl;
    for (int i = 0; i < numEstudiantes; ++i) {
        cout << "Estudiante " << i+1 << ":" << endl;
        for (int j = 0; j < 5; ++j) {
            cout << "Ingrese la calificación " << j+1 << ": ";
            cin >> calificaciones[i][j];
        }
    }

    calcularPromedio(calificaciones, numEstudiantes);

    ordenarCalificaciones(calificaciones, numEstudiantes);

    cout << "Calificaciones ordenadas de cada estudiante:" << endl;
    for (int i = 0; i < numEstudiantes; ++i) {
        cout << "Estudiante " << i+1 << ": ";
        for (int j = 0; j < 5; ++j) {
            cout << calificaciones[i][j] << " ";
        }
        cout << endl;
    }

    int asignatura;
    cout << "Ingrese el número de la asignatura (0-4): ";
    cin >> asignatura;

    int maximaCalificacion = encontrarMaximaCalificacion(calificaciones, numEstudiantes, asignatura);
    cout << "La calificación más alta en la asignatura " << asignatura << " es: " << maximaCalificacion << endl;

    return 0;
}

=========================================================================================================================================
=========================================================================================================================================

  
EJERCIO 2

  #include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int MAX_PRODUCTOS = 100;

struct Producto {
    int codigo;
    string nombre;
    int cantidad;
};

Producto inventario[MAX_PRODUCTOS];
int numProductos = 0;

void agregarProducto() {
    if (numProductos < MAX_PRODUCTOS) {
        cout << "Ingrese el código del producto: ";
        int codigo;
        cin >> codigo;
        cout << "Ingrese el nombre del producto: ";
        string nombre;
        cin.ignore(); // Limpiar el buffer de entrada
        getline(cin, nombre);
        cout << "Ingrese la cantidad en stock: ";
        int cantidad;
        cin >> cantidad;
        
        inventario[numProductos] = {codigo, nombre, cantidad};
        numProductos++;
        cout << "Producto agregado al inventario." << endl;
    } else {
        cout << "No se puede agregar más productos, inventario lleno." << endl;
    }
}

void ordenarInventario() {
    sort(inventario, inventario + numProductos, [](const Producto& a, const Producto& b) {
        return a.nombre < b.nombre;
    });
    cout << "Inventario ordenado por nombre del producto." << endl;
}

void buscarProductoPorCodigo() {
    cout << "Ingrese el código del producto: ";
    int codigo;
    cin >> codigo;
    
    for (int i = 0; i < numProductos; ++i) {
        if (inventario[i].codigo == codigo) {
            cout << "Producto encontrado:" << endl;
            cout << "Código: " << inventario[i].codigo << endl;
            cout << "Nombre: " << inventario[i].nombre << endl;
            cout << "Cantidad en stock: " << inventario[i].cantidad << endl;
            return;
        }
    }
    cout << "Producto no encontrado en el inventario." << endl;
}

void venderProducto() {
    cout << "Ingrese el código del producto: ";
    int codigo;
    cin >> codigo;
    
    for (int i = 0; i < numProductos; ++i) {
        if (inventario[i].codigo == codigo) {
            cout << "Ingrese la cantidad a vender: ";
            int cantidad;
            cin >> cantidad;
            
            if (inventario[i].cantidad >= cantidad) {
                inventario[i].cantidad -= cantidad;
                cout << "Venta realizada. Stock actualizado." << endl;
                return;
            } else {
                cout << "No hay suficiente stock para realizar la venta." << endl;
                return;
            }
        }
    }
    cout << "Producto no encontrado en el inventario." << endl;
}

void recibirStock() {
    cout << "Ingrese el código del producto: ";
    int codigo;
    cin >> codigo;
    
    for (int i = 0; i < numProductos; ++i) {
        if (inventario[i].codigo == codigo) {
            cout << "Ingrese la cantidad a recibir: ";
            int cantidad;
            cin >> cantidad;
            
            inventario[i].cantidad += cantidad;
            cout << "Stock actualizado." << endl;
            return;
        }
    }
    cout << "Producto no encontrado en el inventario." << endl;
}

int main() {
    char opcion;
    do {
        cout << "MENU DE OPCIONES" << endl;
        cout << "1. Agregar producto" << endl;
        cout << "2. Ordenar inventario" << endl;
        cout << "3. Buscar producto por código" << endl;
        cout << "4. Vender producto" << endl;
        cout << "5. Recibir stock" << endl;
        cout << "6. Salir" << endl;
        cout << "Ingrese su opción: ";
        cin >> opcion;
        
        switch (opcion) {
            case '1':
                agregarProducto();
                break;
            case '2':
                ordenarInventario();
                break;
            case '3':
                buscarProductoPorCodigo();
                break;
            case '4':
                venderProducto();
                break;
            case '5':
                recibirStock();
                break;
            case '6':
                cout << "Saliendo del programa." << endl;
                break;
            default:
                cout << "Opción no válida. Inténtelo de nuevo." << endl;
        }
    } while (opcion != '6');

    return 0;
}




=========================================================================================================================================
=========================================================================================================================================

  
EJERCICIO 3 


  #include <iostream>
#include <iomanip>

using namespace std;

const int FILAS = 5;
const int COLUMNAS = 5;

int tablero[FILAS][COLUMNAS];


void inicializarTablero() {
    for (int i = 0; i < FILAS; ++i) {
        for (int j = 0; j < COLUMNAS; ++j) {
            tablero[i][j] = 0;
        }
    }
}


void colocarFicha(int fila, int columna, int tipoFicha) {
    tablero[fila][columna] = tipoFicha;
}

bool buscarLinea(int fila, int columna, int tipoFicha) {
    return false;
}


void imprimirTablero() {
    for (int i = 0; i < FILAS; ++i) {
        for (int j = 0; j < COLUMNAS; ++j) {
            cout << setw(2) << tablero[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
   
    inicializarTablero();
    int fila, columna;
    int tipoFicha = 1;
    for (int turno = 1; turno <= FILAS * COLUMNAS; ++turno) {
        cout << "Turno del Jugador " << tipoFicha << endl;
        imprimirTablero();
        cout << "Jugador " << tipoFicha << ", elige una fila y una columna para colocar tu ficha (fila columna): ";
        cin >> fila >> columna;
        if (fila >= 0 && fila < FILAS && columna >= 0 && columna < COLUMNAS && tablero[fila][columna] == 0) {
            colocarFicha(fila, columna, tipoFicha);
            if (buscarLinea(fila, columna, tipoFicha)) {
                cout << "¡Felicidades! Jugador " << tipoFicha << " ha ganado." << endl;
                break;
            }

           
            tipoFicha = (tipoFicha == 1) ? 2 : 1;
        } else {
           
            cout << "Fila y/o columna inválida. Por favor, elige otra casilla." << endl;
            --turno; 
        }
    }

  
    if (tipoFicha == 1 || tipoFicha == 2) {
        cout << "¡El juego ha terminado en empate!" << endl;
    }
    cout << "Estado final del tablero:" << endl;
    imprimirTablero();

    return 0;
}


=========================================================================================================================================
=========================================================================================================================================

  EJERCIO 4


  #include <iostream>
#include <algorithm>

using namespace std;

const int DIAS=3;
const int HORAS = 3;


void temperaturaPromedioDiaria(double temperaturas[][HORAS]) {
    for (int i = 0; i < DIAS; ++i) {
        double promedio = 0.0;
        for (int j = 0; j < HORAS; ++j) {
            promedio += temperaturas[i][j];
        }
        promedio /= HORAS;
        cout << "Temperatura promedio del día " << i + 1 << ": " << promedio << "°C" << endl;
    }
}

void ordenarTemperaturas(double temperaturas[][HORAS]) {
    for (int i = 0; i < DIAS; ++i) {
        sort(temperaturas[i], temperaturas[i] + HORAS);
    }
}

void encontrarExtremos(double temperaturas[][HORAS]) {
    double maxima = temperaturas[0][0];
    double minima = temperaturas[0][0];
    int diaMaxima = 1;
    int diaMinima = 1;
    for (int i = 0; i < DIAS; ++i) {
        for (int j = 0; j < HORAS; ++j) {
            if (temperaturas[i][j] > maxima) {
                maxima = temperaturas[i][j];
                diaMaxima = i + 1;
            }
            if (temperaturas[i][j] < minima) {
                minima = temperaturas[i][j];
                diaMinima = i + 1;
            }
        }
    }
    cout << "Día con la temperatura más alta: " << diaMaxima << " (Temperatura: " << maxima << "°C)" << endl;
    cout << "Día con la temperatura más baja: " << diaMinima << " (Temperatura: " << minima << "°C)" << endl;
}

int main() {
    double temperaturas[DIAS][HORAS];

    cout << "Ingrese las temperaturas diarias para " << DIAS << " días y " << HORAS << " horas por día:" << endl;
    for (int i = 0; i < DIAS; ++i) {
        cout << "Día " << i + 1 << ":" << endl;
        for (int j = 0; j < HORAS; ++j) {
            cout << "Temperatura para la hora " << j + 1 << ": ";
            cin >> temperaturas[i][j];
        }
    }

    temperaturaPromedioDiaria(temperaturas);
    ordenarTemperaturas(temperaturas);
    encontrarExtremos(temperaturas);

    return 0;
}





=========================================================================================================================================
=========================================================================================================================================

  
EJERCICIO 5



  #include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_CIUDADES = 10;

void ingresarDistancias(vector<vector<int>>& distancias) {
    int numCiudades = distancias.size();
    cout << "Ingrese las distancias entre las ciudades:" << endl;
    for (int i = 0; i < numCiudades; ++i) {
        for (int j = 0; j < numCiudades; ++j) {
            cout << "Distancia de la ciudad " << i + 1 << " a la ciudad " << j + 1 << ": ";
            cin >> distancias[i][j];
        }
    }
}

int sumaDistanciasCiudad(const vector<vector<int>>& distancias, int ciudad) {
    int suma = 0;
    for (int j = 0; j < distancias.size(); ++j) {
        suma += distancias[ciudad][j];
    }
    return suma;
}

bool compararDistanciasTotales(const pair<int, int>& ciudad1, const pair<int, int>& ciudad2, const vector<vector<int>>& distancias) {
    return sumaDistanciasCiudad(distancias, ciudad1.first) < sumaDistanciasCiudad(distancias, ciudad2.first);
}

void ordenarCiudadesPorDistanciaTotal(const vector<vector<int>>& distancias) {
    vector<pair<int, int>> ciudades;
    for (int i = 0; i < distancias.size(); ++i) {
        ciudades.push_back({i, sumaDistanciasCiudad(distancias, i)});
    }
    sort(ciudades.begin(), ciudades.end(), [&](const pair<int, int>& ciudad1, const pair<int, int>& ciudad2) {
        return compararDistanciasTotales(ciudad1, ciudad2, distancias);
    });

    cout << "Ciudades ordenadas por su distancia total a todas las demás:" << endl;
    for (const auto& ciudad : ciudades) {
        cout << "Ciudad " << ciudad.first + 1 << ": Distancia total = " << ciudad.second << endl;
    }
}

int distanciaMinimaEntreCiudades(const vector<vector<int>>& distancias, int ciudad1, int ciudad2) {
    return distancias[ciudad1][ciudad2];
}

void imprimirMatrizDistancias(const vector<vector<int>>& distancias) {
    cout << "Matriz de distancias entre ciudades:" << endl;
    for (int i = 0; i < distancias.size(); ++i) {
        for (int j = 0; j < distancias[i].size(); ++j) {
            cout << setw(4) << distancias[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int numCiudades;
    cout << "Ingrese el número de ciudades (máximo " << MAX_CIUDADES << "): ";
    cin >> numCiudades;

    if (numCiudades < 2 || numCiudades > MAX_CIUDADES) {
        cout << "Número de ciudades no válido." << endl;
        return 1;
    }

    vector<vector<int>> distancias(numCiudades, vector<int>(numCiudades));

    ingresarDistancias(distancias);

    imprimirMatrizDistancias(distancias);

    ordenarCiudadesPorDistanciaTotal(distancias);

    int ciudad1, ciudad2;
    cout << "Ingrese el número de las dos ciudades para encontrar la distancia mínima entre ellas (1-" << numCiudades << "): ";
    cin >> ciudad1 >> ciudad2;
    if (ciudad1 < 1 || ciudad1 > numCiudades || ciudad2 < 1 || ciudad2 > numCiudades) {
        cout << "Números de ciudades no válidos." << endl;
        return 1;
    }
    cout << "La distancia mínima entre la Ciudad " << ciudad1 << " y la Ciudad " << ciudad2 << " es: " << distanciaMinimaEntreCiudades(distancias, ciudad1 - 1, ciudad2 - 1) << endl;

    return 0;
}

=========================================================================================================================================
=========================================================================================================================================

  
EJERCICIO 6
  #include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

const int ESTUDIANTES = 5;
const int MATERIAS = 3;

void ingresarNotas(int notas[][MATERIAS]) {
    cout << "Ingrese las notas de los estudiantes para " << MATERIAS << " materias y " << ESTUDIANTES << " estudiantes:" << endl;
    for (int i = 0; i < ESTUDIANTES; ++i) {
        cout << "Estudiante " << i + 1 << ":" << endl;
        for (int j = 0; j < MATERIAS; ++j) {
            cout << "Nota para la materia " << j + 1 << ": ";
            cin >> notas[i][j];
        }
    }
}

void calcularPromedios(const int notas[][MATERIAS]) {
    for (int i = 0; i < ESTUDIANTES; ++i) {
        double promedio = 0.0;
        for (int j = 0; j < MATERIAS; ++j) {
            promedio += notas[i][j];
        }
        promedio /= MATERIAS;
        cout << "El promedio de notas del Estudiante " << i + 1 << " es: " << fixed << setprecision(2) << promedio << endl;
    }
}

void ordenarNotas(int notas[][MATERIAS]) {
    for (int i = 0; i < ESTUDIANTES; ++i) {
        sort(notas[i], notas[i] + MATERIAS, greater<int>());
    }
}

int encontrarNotaMaxima(const int notas[][MATERIAS], int materia) {
    int maxima = notas[0][materia];
    for (int i = 1; i < ESTUDIANTES; ++i) {
        maxima = max(maxima, notas[i][materia]);
    }
    return maxima;
}

int encontrarNotaMinima(const int notas[][MATERIAS], int materia) {
    int minima = notas[0][materia];
    for (int i = 1; i < ESTUDIANTES; ++i) {
        minima = min(minima, notas[i][materia]);
    }
    return minima;
}

void imprimirDatos(const int notas[][MATERIAS], int materia) {
    cout << "Notas de los estudiantes:" << endl;
    for (int i = 0; i < ESTUDIANTES; ++i) {
        cout << "Estudiante " << i + 1 << ": ";
        for (int j = 0; j < MATERIAS; ++j) {
            cout << notas[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    cout << "Promedios de notas:" << endl;
    calcularPromedios(notas);
    cout << endl;

    cout << "Notas más alta y más baja en la materia " << materia + 1 << ":" << endl;
    cout << "Nota más alta: " << encontrarNotaMaxima(notas, materia) << endl;
    cout << "Nota más baja: " << encontrarNotaMinima(notas, materia) << endl;
}

int main() {
    int notas[ESTUDIANTES][MATERIAS];

    ingresarNotas(notas);

    ordenarNotas(notas);

    int materia;
    cout << "Ingrese el número de la materia para encontrar las notas más alta y más baja (1-" << MATERIAS << "): ";
    cin >> materia;
    if (materia < 1 || materia > MATERIAS) {
        cout << "Número de materia no válido." << endl;
        return 1;
    }

    imprimirDatos(notas, materia - 1);

    return 0;
}


