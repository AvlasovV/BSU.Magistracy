﻿/**
Имя входного файла: matrix.in
Имя выходного файла: matrix.out
Ограничение по времени: 1 с
Ограничение по памяти: 1024 МБ
Маленький Джон изучает, как перемножать матрицы. Он упражняется в умножении больших бинарных матриц над полем F2 (все операции в этом поле выполняются по модулю 2).
Недавно он умножил две матрицы A и B размера n×n и утверждает, что результат равен C.
Но Женя не верит ему. Она говорит, что результат неверный. Помогите детям решить их спор. По матрицам A, B и C определите, правда ли, что AB = C.
Формат входных данных
Первая строка содержит число n — размер матриц (1≤n≤4000). Следующие 3 строки описывают матрицы A, B и C.
Каждая матрица описывается строкой, которая содержит n блоков по ⌈n / 4⌉ шестнадцатеричных цифр. (n / 4 с округлением вверх)
Если записать цифры в двоичном представлении от старшего бита к младшему и обрезать лишние знаки в конце, то получится соответствующая строка матрицы.

Формат выходных данных
Выведите YES, если равенство AB = C верно, или NO в противном случае.
Пример
matrix.in	matrix.out
6
28 A8 68 78 D0 88
80 40 20 10 08 04
28 A8 68 78 D0 88
YES
6
28 A8 68 78 D0 88
80 40 20 10 08 04
28 B8 68 78 D0 88
NO
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

using namespace std;

void read_matrix(int n, int blocksize){
    var matrix = new [n];
    char* lines = new char[n*block];
    getline(cin, lines);
    for (int i = 0; i < n; i++){
        int iLine = new int[blocksize];
        char hexDigits = lines[i];
        for (int j = 0; j < hexDigits.Length; j++)
        {
            int fourBits = hexDigits[j] >= 'A' ? hexDigits[j] - 'A' + 10 : hexDigits[j] - '0';
            var requiredBits = min(4, n - j * 4);
            fourBits &= ((1 << (requiredBits + 1)) - 1) << (4 - requiredBits);

            iLine[j / 8] |= fourBits << (28 - 4 * (j % 8));
        }
        matrix[i] = new BitArray(iLine);
    }
}

int main()
{
//	long a = 0;
//	scanf("%x", &a);
//	char bin[100];
//	sprintf(buf,"%d",i); //_itoa_s(a, bin, 100, 2);
//	int i = 0;
//	while (bin[i] != '\0')
//		printf("%c", bin[i++]);
//	_getch();
//	return 0;
    int n;
    cin >> n;
    int blocksize = n / 32 + (n % 32 > 0 ? 1 : 0);
    read_matrix(n, blocksize);
}
