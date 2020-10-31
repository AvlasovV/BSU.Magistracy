/**
Требуется вычислить произведение матрицы на вектор. Все операции нужно производить по модулю 256.

Формат входных данных
Первые 4 байта входного файла задают число N строк в матрице (1 N). Далее 4 байта задают число M столбцов (1≤M).
Следующие N×M байт задают элементы матрицы (по одному байту на каждый элемент матрицы), строки записаны в порядке от 1 до N.
Следующие M байт задают элементы вектора (по одному байту на каждый элемент вектора).
Общий объем входного файла не превосходит 13500000 байт.
Формат выходных данных
Выведите N байт, задающие элементы результирующего вектора.
Пример
input.bin
3 4
1 2 3 4
5 6 7 8
9 0 0 0
1
2
3
4
output.bin
30
70
9
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <stdlib.h>

using namespace std;
typedef long long ll;


int B = 1000;
int N;
int M;


void read_block(string filename){
    ifstream input_file;
    input_file.open(filename, ios::in | ios::binary);
    input_file.read((char*)&N, sizeof(int));

    input_file.read((char*)block, NUM_SIZE * N);
    ll * block = new ll[N];
    input_file.close();

    cout << endl << "File = " << filename << ", N = " << N << endl;
    for(ll i = 0; i < N; i++){
        cout << block[i] << endl;
    }
    delete []block;

}

int main(){

}
