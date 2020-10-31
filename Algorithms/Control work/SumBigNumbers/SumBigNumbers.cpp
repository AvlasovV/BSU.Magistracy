/**
В этой задаче вам нужно только сложить два числа, два длинных числа.

Формат входных данных
Входные данные представлены в следующем формате: целое число n (4 байта) — длина числа A в цифрах,
далее следуют n байт, задающие цифры числа A; целое число m (4 байта) — длина числа B в цифрах,
далее следуют m байт, задающие цифры числа B.
Входные данные удовлетворяют следующим ограничениям: 1≤n,m≤5000000, 0≤A,B.
Формат выходных данных
Выведите целое число k (4 байта) — длину числа C в цифрах (C=A+B), далее выведите k байт, задающих цифры числа C.
Пример
input.bin
1 4
2 1 6

output.bin
2 2 0
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <stdlib.h>

using namespace std;

int B = 1;
int n;
int m;
int INT_SIZE = sizeof(int);
int CHAR_SIZE = sizeof(char);
int m_start, n_start = INT_SIZE;

void write_binary(string filename){
    ofstream output_file;
    int k1 = 2, k2 = 4;
    char block1[] = {'1', '2'}; //, '3', '4', '0'};
    char block2[] = {'5', '0', '4', '1'};  //,'5', '4', '5', '3'};

    output_file.open(filename, ios::out | ios::binary);

    output_file.write((char*)&k1, INT_SIZE);
    output_file.write(&block1[0], k1 * CHAR_SIZE);

    output_file.write((char*)&k2, INT_SIZE);
    output_file.write(&block2[0], k2 * CHAR_SIZE);

    output_file.close();
}

void read_and_print(string filename){
    ifstream input_file;
    input_file.open(filename, ios::in | ios::binary);
    int l;
    input_file.read((char*)&l, INT_SIZE);
    vector<char> block;
    block.reserve(l);

    input_file.read(&block[0], CHAR_SIZE * n);
    int sum = 0;
    cout << "Count: " << l << endl;
    for(int i = 0; i < l; i++){
        cout << (int)block[i] << " ";
        sum += block[i];
    }
    cout << endl << sum << "\n";

    input_file.close();
}

void read_sizes(string filename){
    ifstream input_file;
    input_file.open(filename, ios::in | ios::binary);

    input_file.read((char*)&n, INT_SIZE);


    vector<char> block;
    block.reserve(n);

    input_file.read(&block[0], CHAR_SIZE * n);
    int sum = 0;
    for(int i = 0; i < n; i++){
        cout << (int)block[i] -  '0' << " ";
        sum += block[i];
    }
    cout << endl << sum << "\n";

    input_file.seekg(INT_SIZE + n, input_file.beg);
    input_file.read((char*)&m, INT_SIZE);

    m_start = INT_SIZE * 2 + n;

    cout << n << " " << m << endl;

    input_file.close();
}

void read_block(vector<char> &block, ifstream &input_f, int length){
    input_f.read(&block[0], CHAR_SIZE * length);
}

int main(){

    string filename = "input_test.bin";
    write_binary(filename);

    read_sizes(filename);

    int min_number = min(n, m);
    int max_number = max(n, m) + 1;
    int double_iterations = (min_number / B) + 1;


    ifstream input_n, input_m;
    input_n.open(filename, ios::in | ios::binary);
    input_m.open(filename, ios::in | ios::binary);

    ofstream output_f;
    output_f.open("output.bin", ios::out | ios::binary);
    output_f.write((char*)&max_number, INT_SIZE);

    vector<char> n_vector;
    vector<char> m_vector;
    vector<char> out_vector;
    n_vector.reserve(B);
    m_vector.reserve(B);
    out_vector.reserve(B);

    int remaining_n = n, remaining_m = m; // how much more should we read
    int leng = B;
    char sum;
    char previous_one = 0;

    for(int i = 0; i < double_iterations; i++){
        if (min_number >= B){
            input_n.seekg(n_start + n - ((i + 1) * B));
            input_m.seekg(m_start + m - ((i + 1) * B));
            min_number -= B;
            read_block(n_vector, input_n, B);
            read_block(m_vector, input_m, B);
        }
        else{
            input_n.seekg(n_start + n - (i * B) - min_number);
            input_m.seekg(m_start + m - (i * B) - min_number);
            read_block(n_vector, input_n, min_number);
            read_block(m_vector, input_m, min_number);
            leng = min_number;
            min_number = 0;
        }

        for(int j = leng - 1; j >=0; j--){
            sum = ((m_vector[j] - '0') + (n_vector[j] - '0')) + previous_one;
            out_vector.insert(out_vector.begin(), sum % 10);
            if ((sum / 10) >= 1){
                previous_one = 1;
            }
            else{
                previous_one = 0;
            }
        }
        cout << "Output vector on " << i << " iteration:" << endl;
        for(int k = 0; k < leng; k++){
            cout << (int)out_vector[k] << " ";
        }
        cout << endl;
        output_f.write(&out_vector[0], leng * CHAR_SIZE);

    }


    int remain = abs(n - m);
    int iterations = (remain / B) + 1;
    leng = B;

    if(n > m){
        for(int i = 0; i < iterations; i++){

            if (remain >= B){
                input_n.seekg(n_start + m - ((i + 1) * B));
                remain -= B;
                read_block(n_vector, input_n, B);
            }
            else{
                input_n.seekg(n_start + m - (i * B) - remain);
                read_block(n_vector, input_n, remain);
                leng = remain;
                remain = 0;
            }

            for(int j = leng - 1; j >=0; j--){
                sum = ((n_vector[j] - '0')) + previous_one;
                out_vector.insert(out_vector.begin(), sum % 10);
                if ((sum / 10) >= 1){
                    previous_one = 1;
                }
                else{
                    previous_one = 0;
                }
            }
            output_f.write(&out_vector[0], leng * CHAR_SIZE);

        }
    }
    else{
        for(int i = 0; i < iterations; i++){

            if (remain >= B){
                input_m.seekg(m_start + n - ((i + 1) * B));
                remain -= B;
                read_block(m_vector, input_m, B);
            }
            else{
                input_m.seekg(m_start + n - (i * B) - remain);
                read_block(m_vector, input_m, remain);
                leng = remain;
                remain = 0;
            }

            for(int j = leng - 1; j >=0; j--){
                sum = ((m_vector[j] - '0')) + previous_one;
                out_vector.insert(out_vector.begin(), sum % 10);
                if ((sum / 10) >= 1){
                    previous_one = 1;
                }
                else{
                    previous_one = 0;
                }
            }
            output_f.write(&out_vector[0], leng * CHAR_SIZE);
        }
    }

    if(previous_one > 0){
        char a = '1';
        output_f.write(&a, CHAR_SIZE);
    }


    output_f.close();
    input_n.close();
    input_m.close();

    read_and_print("output.bin");

}
