/**
Требуется отсортировать файл с целыми числами во внешней памяти.

Input
Первые 8 байт входного файла задают число N элементов в массиве, который нужно отсортировать (1≤N).
Следующие 8×N байт задают элементы массива (по восемь байт на каждый элемент массива). Все числа в массиве положительные и не превосходят 260.
Общий объем входного файла не превосходит 10240008 байт.

Output
Выведите отсортированный массив в таком же формате, как представлен входной.
Example
input.bin
5 5 3 4 2 1
output.bin
5 1 2 3 4 5
Note
Пример в задаче приведён в текстовом формате для пояснения. Входной файл в бинарном формате.
Если ваше решение использует более 700 МБ, то места для создания дополнительных файлов может не хватить.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;
typedef long long ll;


int BLOCK_SIZE = 5;
ll file_counter = 0;

void write_sequence_into_file(vector<ll> seq, char* filename){
    ofstream output_file;
    output_file.open(filename, ios::out | ios:: binary);
    ll seq_length = seq.size();
    output_file.write((char*)&seq_length, sizeof(ll));
    ll buf;
    for (int i = 0; i < seq.size(); i++){
        buf = seq[i];
        output_file.write((char*)&buf, sizeof(ll));
    }
    output_file.close();
}

ll read_and_sort(const char* s){
    ifstream input_file;
    ll N;
    ll buf;
    vector<ll> input_sequence;
    input_file.open(s, ios::in | ios::binary);
    input_file.read((char*)&N, sizeof(ll));
    for(ll i; i < N; i++){
        input_file.read((char*)&buf, sizeof(ll));
        if(input_sequence.size() < BLOCK_SIZE){
            input_sequence.push_back(buf);
        }
        else{
            sort(input_sequence.begin(), input_sequence.end());
            string file_name = "sorted" + to_string(file_counter);
            char file_n[file_name.size()+1];
            //char *file_n = new char[file_name.size()+1];
            strcpy(file_n, file_name.c_str());
            write_sequence_into_file(input_sequence, file_n);
            input_sequence.clear();
            input_sequence.shrink_to_fit();
            file_counter++;
        }
    }
    if(input_sequence.size() > 0){
            sort(input_sequence.begin(), input_sequence.end());
            string file_name = "sorted" + to_string(file_counter);
            char file_n[file_name.size()+1];
            //char *file_n = new char[file_name.size()+1];
            strcpy(file_n, file_name.c_str());
            write_sequence_into_file(input_sequence, file_n);
            input_sequence.clear();
            input_sequence.shrink_to_fit();
            file_counter++;
    }
    return N;
}

int main(){

    ifstream input_file;
    ll N = read_and_sort("input.bin");

//cout << "N = " << N << endl;





//    for(ll i = 0; i < N; i++){
//        input_file.read((char*)&buf, sizeof(ll));
//        input_sequence.push_back(buf);
//    }
// for(ll i  =                 0; i     < input_sequence.size(); i++){
// cout   << input_sequence[i] << endl;
// }
//    ofstream output_file;
//    output_file.open("output.bin", ios::out | ios:: binary);
//    output_file.write((char*)&M, sizeof(int));
//    output_file.write((char*)&N, sizeof(int));
//    output_file.close();
//
//    input_file.open("output.bin", ios::in | ios::binary);
//    input_file.read((char*)&N, sizeof(int));
//    input_file.read((char*)&M, sizeof(int));
//
//    cout << N << " " << M;
////    input_file.read((char*)&N, sizeof(int));
////    input_file.read((char*)&M, sizeof(int));
////
////    cout << N << " " << M;
////
////    output_file.write((char*)&M, sizeof(int));
////    output_file.write((char*)&N, sizeof(int));
//
//
//
////    vector<char> block;
////    block.reserve(N * M);
////
////    input_file.seekg(2 * sizeof(int), input_file.beg);
////    input_file.read(&block[0], sizeof(char) * N * M);
////
////    if (N != M) {
////        tranpose_asymetric(block, N, M);
////    } else {
////        transpose(block, N);
////    }
////
////    output_file.seekp(2 * sizeof(int), output_file.beg);
////    output_file.write(&block[0], N * M * sizeof(char));
//    input_file.close();
//    //output_file.close();

}
