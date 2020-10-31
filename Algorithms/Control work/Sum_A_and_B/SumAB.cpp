/**
В этой задаче вам нужно только сложить два числа.

Формат входных данных
Входной файл содержит два целых числа A и B (1≤A,B≤10^6).
Числа записаны в бинарном формате (т.е. размер входного файла равен 8 байт).
Формат выходных данных
Выведите одно целое число (4 байта).
*/
#include <iostream>
#include <fstream>

#include <stdlib.h>
using namespace std;

int main(){
    ifstream input_file;
    input_file.open("input.bin", ios::in | ios::binary);
    int a, b;
    input_file.read((char*)&a, sizeof(int));
    input_file.read((char*)&b, sizeof(int));
    a = a + b;
    cout << a;
    input_file.close();
    ofstream output_file;
    output_file.open("output.bin", ios::out | ios:: binary);
    output_file.write((char*)&a, sizeof(int));
    output_file.close();
}
