/**
Требуется отсортировать файл с целыми числами во внешней памяти.

Input
Первые 8 байт входного файла задают число N элементов в массиве, который нужно отсортировать (1≤N).
Следующие 8×N байт задают элементы массива (по восемь байт на каждый элемент массива). Все числа в массиве положительные и не превосходят 2^60.
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
#include <stdlib.h>

using namespace std;
typedef long long ll;


int BLOCK_SIZE = 4000;
int NUM_SIZE = sizeof(ll);
ll file_counter = 0;

void write_sequence_into_file(vector<ll> seq, string filename){
    ofstream output_file;
    output_file.open(filename, ios::out | ios:: binary);
    ll seq_length = seq.size();
    output_file.write((char*)&seq_length, NUM_SIZE);
    ll buf;
    for (int i = 0; i < seq.size(); i++){
        buf = seq[i];
        output_file.write((char*)&buf, NUM_SIZE);
    }
    output_file.close();
}

ll read_and_sort(char* f_name){

    ifstream input_file;
    ll N;
    ll buf;
    vector<ll> input_sequence;
    input_file.open(f_name, ios::in | ios::binary);
    input_file.read((char*)&N, NUM_SIZE);
    for(ll i = 0; i < N; i++){
        if(input_sequence.size() < BLOCK_SIZE){
            input_file.read((char*)&buf, NUM_SIZE);
            input_sequence.push_back(buf);
        }
        else{
            sort(input_sequence.begin(), input_sequence.end());

//            string file_name = to_string(file_counter);
//            char file_n[file_name.size()+1];
//            strcpy(file_n, file_name.c_str());
//            write_sequence_into_file(input_sequence, file_n);

            write_sequence_into_file(input_sequence, to_string(file_counter));
            input_sequence.clear();
            input_sequence.shrink_to_fit();

            input_file.read((char*)&buf, NUM_SIZE);
            input_sequence.push_back(buf);
            file_counter++;
        }
    }
    if(input_sequence.size() > 0){
            sort(input_sequence.begin(), input_sequence.end());

//            string file_name = to_string(file_counter);
//            char file_n[file_name.size()+1];
//            strcpy(file_n, file_name.c_str());
//            write_sequence_into_file(input_sequence, file_n);
            write_sequence_into_file(input_sequence, to_string(file_counter));
            input_sequence.clear();
            input_sequence.shrink_to_fit();
            file_counter++;
    }
    return N;
}

void read_and_print(string filename){
    ifstream input_file;
    input_file.open(filename, ios::in | ios::binary);
    ll N;
    ll buf;
    input_file.read((char*)&N, NUM_SIZE);
    cout << "N = " << N << endl;
    for(ll i = 0; i < N; i++){
        input_file.read((char*)&buf, NUM_SIZE);
        cout << buf << endl;
    }
    input_file.close();
}

void merge_two_files(string f1, string f2, bool out = false){
    ifstream file1, file2;
    file1.open(f1, ios::in | ios::binary);
    file2.open(f2, ios::in | ios::binary);

    ll len1, len2, big_len;
    file1.read((char*)&len1, NUM_SIZE);
    file2.read((char*)&len2, NUM_SIZE);
    big_len = len1 + len2;

//    string file_name = to_string(file_counter);
//    char file_n[file_name.size()+1];
//    strcpy(file_n, file_name.c_str());
    string file_n;
    if(!out){
        file_n = to_string(file_counter);
        file_counter++;
    }
    else{
        file_n = "output.bin";
    }
    ofstream output_file;
    output_file.open(file_n, ios::out | ios:: binary);
    output_file.write((char*)&big_len, NUM_SIZE);

    ll buf1, buf2;
    file1.read((char*)&buf1, NUM_SIZE);
    file2.read((char*)&buf2, NUM_SIZE);
    len1--;
    len2--;
    while(1){
        if(buf1 < buf2){
            output_file.write((char*)&buf1, NUM_SIZE);
            file1.read((char*)&buf1, NUM_SIZE);
            len1--;
        }
        else{
            output_file.write((char*)&buf2, NUM_SIZE);
            file2.read((char*)&buf2, NUM_SIZE);
            len2--;
        }
        if(len1 < 0){
            output_file.write((char*)&buf2, NUM_SIZE);
            for(ll i = 0; i < len2; i++){
                file2.read((char*)&buf2, NUM_SIZE);
                output_file.write((char*)&buf2, NUM_SIZE);
            }
            break;
        }
        else if(len2 < 0){
            output_file.write((char*)&buf1, NUM_SIZE);
            for(ll i = 0; i < len1; i++){
                file1.read((char*)&buf1, NUM_SIZE);
                output_file.write((char*)&buf1, NUM_SIZE);
            }
            break;
        }
    }
    file1.close();
    file2.close();
    output_file.close();
}


void merge_all(){
    if(file_counter > 1){
        ll cur_iteration = 0;
        while(file_counter - cur_iteration > 2){
            ll cur_counter = file_counter;
            for(ll i = cur_iteration; i < cur_counter - 1; i += 2){
                merge_two_files(to_string(i), to_string(i+1));
            }
            cur_iteration = cur_counter;
            if(cur_counter % 2 == 1){
                merge_two_files(to_string(cur_counter - 1),to_string(cur_counter));
                cur_iteration++;
            }
        }
        if(file_counter - cur_iteration == 2){
            merge_two_files(to_string(file_counter - 1),to_string(cur_iteration), true );
        }
        //merge_two_files(to_string(file_counter - 1),to_string(cur_iteration), true );
        if(file_counter - cur_iteration == 1){
            string file_name = to_string(file_counter-1);
            char file_n[file_name.size()+1];
            strcpy(file_n, file_name.c_str());
            rename(file_n, "output.bin");
        }
    }
    else{
        string file_name = to_string(file_counter - 1);
        char file_n[file_name.size()+1];
        strcpy(file_n, file_name.c_str());
        rename(file_n, "output.bin");
    }
}

int main(){


//    read_and_print("input.bin");
    ll N = read_and_sort("input.bin");
    merge_all();
//    read_and_print("output.bin");
//    read_and_print("0");
//    rename("0", "pampam");
//    read_and_print("pampam");
//    cout << "Sorted files = " << file_counter << endl;

//    char buf[20];
//    int num = 100000;
////    char *p = itoa(num, buf, 10);
//    char *p = to_string(num).c_str;
//    cout << p << endl;
//    cout << "N = " << N << endl;
//    merge_two_files("0", "2");
//    read_and_print("0");
//    read_and_print("1");
//    read_and_print("2");
//    cout << "Merged\n";
//    read_and_print("3");

//cout << "N = " << N << endl;
//    for(ll i = 0; i < N; i++){
//        input_file.read((char*)&buf, NUM_SIZE);
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
