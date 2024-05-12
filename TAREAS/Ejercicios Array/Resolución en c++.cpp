// Resolucion 1

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cout << "Ingrese el número de personas: ";
    cin >> N;

    vector<double> alturas(N);
    double suma = 0;

    for (int i = 0; i < N; ++i) {
        cout << "Ingrese la altura de la persona " << i+1 << ": ";
        cin >> alturas[i];
        suma += alturas[i];
    }

    double media = suma / N;
    int mayores = 0, menores = 0;

    for (int i = 0; i < N; ++i) {
        if (alturas[i] > media) {
            mayores++;
        } else if (alturas[i] < media) {
            menores++;
        }
    }

    cout << "Altura media: " << media << endl;
    cout << "Personas con altura superior a la media: " << mayores << endl;
    cout << "Personas con altura inferior a la media: " << menores << endl;

    return 0;
}


//Resolución 2

#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> numeros(10);

    cout << "Ingrese 10 numeros enteros separados por espacio: ";
    for (int i = 0; i < 10; ++i) {
        cin >> numeros[i];
    }

    int suma_positivos = 0, suma_negativos = 0;
    int count_positivos = 0, count_negativos = 0;

    for (int num : numeros) {
        if (num > 0) {
            suma_positivos += num;
            count_positivos++;
        } else if (num < 0) {
            suma_negativos += num;
            count_negativos++;
        }
    }

    if (count_positivos > 0) {
        cout << "Media de los valores positivos: " << static_cast<double>(suma_positivos) / count_positivos << endl;
    } else {
        cout << "No hay valores positivos en el array." << endl;
    }

    if (count_negativos > 0) {
        cout << "Media de los valores negativos: " << static_cast<double>(suma_negativos) / count_negativos << endl;
    } else {
        cout << "No hay valores negativos en el array." << endl;
    }

    return 0;
}


//Resolucion 3


#include <iostream>

using namespace std;

int main() {
    int numeros[10];
    int positivos = 0, negativos = 0, ceros = 0;

    cout << "Ingrese 10 nimeros enteros separados por espacio: ";
    for (int i = 0; i < 10; ++i) {
        cin >> numeros[i];
        if (numeros[i] > 0) {
            positivos++;
        } else if (numeros[i] < 0) {
            negativos++;
        } else {
            ceros++;
        }
    }

    cout << "Cantidad de numeros positivos: " << positivos << endl;
    cout << "Cantidad de números negativos: " << negativos << endl;
    cout << "Cantidad de ceros: " << ceros << endl;

    return 0;
}


//resolucion 4


#include <iostream>
#include <vector>

using namespace std;

int numeroAlumnos() {
    int N;
    cout << "Ingrese el numero de alumnos de la clase: ";
    cin >> N;
    return N;
}

void leerAlturas(vector<double>& alturas, int N) {
    alturas.resize(N);
    for (int i = 0; i < N; ++i) {
        cout << "Ingrese la altura del alumno " << i+1 << ": ";
        cin >> alturas[i];
    }
}

double calcularMedias(const vector<double>& alturas) {
    double suma = 0;
    for (double altura : alturas) {
        suma += altura;
    }
    return suma / alturas.size();
}

void mostrarResultados(const vector<double>& alturas, double media) {
    int mayores = 0, menores = 0;
    for (double altura : alturas) {
        if (altura > media) {
            mayores++;
        } else if (altura < media) {
            menores++;
        }
    }
    cout << "Altura media de los alumnos: " << media << endl;
    cout << "Cantidad de alumnos mas altos que la media: " << mayores << endl;
    cout << "Cantidad de alumnos mas bajos que la media: " << menores << endl;
}

int main() {
    int N = numeroAlumnos();
    vector<double> alturas;
    leerAlturas(alturas, N);
    double media = calcularMedias(alturas);
    mostrarResultados(alturas, media);
    return 0;
}
