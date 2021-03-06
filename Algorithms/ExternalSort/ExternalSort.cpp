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
Если ваше решение использует более 700 МБ, то места для создания дополнительных файлов может не хватить.2
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


int BLOCK_SIZE = 17000;
int NUM_SIZE = sizeof(ll);
ll file_counter = 0;


void read_and_print(string filename){
    ifstream input_file;
    input_file.open(filename, ios::in | ios::binary);
    ll N;
    input_file.read((char*)&N, NUM_SIZE);
    ll * block = new ll[N];
    input_file.read((char*)block, NUM_SIZE * N);
    input_file.close();

    cout << endl << "File = " << filename << ", N = " << N << endl;
    for(ll i = 0; i < N; i++){
        cout << block[i] << endl;
    }
    delete []block;


}

void write_sequence_into_file(ll * seq, ll array_length, string filename){
    ofstream output_file;
    output_file.open(filename, ios::out | ios:: binary);
    output_file.write((char*)&array_length, NUM_SIZE);
    ll buf;
    output_file.write((char*)seq, NUM_SIZE * array_length);
    output_file.close();
}


ll read_and_sort(char* f_name){

    ifstream input_file;
    ll N;
    ll buf;
    ll current_counter = 0;
    ll current_length = BLOCK_SIZE;
    //vector<ll> input_sequence;
    ll * block = new ll[BLOCK_SIZE];
    input_file.open(f_name, ios::in | ios::binary);
    input_file.read((char*)&N, NUM_SIZE);

    while(current_counter < N){
        if(N - current_counter >= BLOCK_SIZE){
            input_file.read((char*)block, NUM_SIZE * BLOCK_SIZE);
            current_counter += current_length;
        }
        else{
            current_length = N - current_counter;
            input_file.read((char*)block, NUM_SIZE * current_length);
            current_counter += current_length;
        }
        sort(block, block + current_length);
        write_sequence_into_file(block, current_length, to_string(file_counter));
        file_counter++;
    }
    delete []block;
    return N;
}


void read_block(ll file_length, ll &counter, ll &cur_length, ll * block, ifstream &input_stream){
    if(file_length - counter >= BLOCK_SIZE){
        input_stream.read((char*)block, NUM_SIZE * BLOCK_SIZE);
        counter += BLOCK_SIZE;
    }
    else{
        cur_length = file_length - counter;
        input_stream.read((char*)block, NUM_SIZE * (cur_length));
        counter = file_length;
    }
}


void merge_two_files(string f1, string f2, bool out = false){
    ifstream file1, file2;
    file1.open(f1, ios::in | ios::binary);
    file2.open(f2, ios::in | ios::binary);

    ll file_len1, file_len2, big_len;
    file1.read((char*)&file_len1, NUM_SIZE);
    file2.read((char*)&file_len2, NUM_SIZE);
    big_len = file_len1 + file_len2;

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

    int arr_iter1 = 0, arr_iter2 = 0, output_iter = 0;
    ll * block1, *block2, *output_block;
    ll counter1 = 0, counter2 = 0, output_counter = 0; //how many elems we have already read
    ll cur_len1 = BLOCK_SIZE;                          // current length of block 1
    ll cur_len2 = BLOCK_SIZE;

    block1 = new ll[BLOCK_SIZE];
    block2 = new ll[BLOCK_SIZE];
    output_block = new ll[BLOCK_SIZE];

    read_block(file_len1, counter1, cur_len1, block1, file1);
    read_block(file_len2, counter2, cur_len2, block2, file2);

    while(output_counter < big_len){
        if(block1[arr_iter1] < block2[arr_iter2]){
            output_block[output_iter] = block1[arr_iter1];
            arr_iter1++;
        }
        else{
            output_block[output_iter] = block2[arr_iter2];
            arr_iter2++;
        }
        output_iter++;
        output_counter++;

        if((output_iter == BLOCK_SIZE) || (output_counter == big_len)){
            output_file.write((char*)output_block, NUM_SIZE * output_iter);
            output_iter = 0;
        }

        if(arr_iter1 == cur_len1){
            if(counter1 >= file_len1){
                output_file.write((char*)output_block, NUM_SIZE * output_iter);
                output_file.write((char*)(block2 + arr_iter2), NUM_SIZE * (cur_len2 - arr_iter2));
                while(counter2 < file_len2){
                    read_block(file_len2, counter2, cur_len2, block2, file2);
                    output_file.write((char*)block2, NUM_SIZE * cur_len2);
                }
                break;
            }
            arr_iter1 = 0;
            read_block(file_len1, counter1, cur_len1, block1, file1);
        }
        if(arr_iter2 == cur_len2){
            if(counter2 >= file_len2){
                output_file.write((char*)output_block, NUM_SIZE * output_iter);
                output_file.write((char*)(block1 + arr_iter1), NUM_SIZE * (cur_len1 - arr_iter1));
                while(counter1 < file_len1){
                    read_block(file_len1, counter1, cur_len1, block1, file1);
                    output_file.write((char*)block1, NUM_SIZE * cur_len1);
                }
                break;
            }
            arr_iter2 = 0;
            read_block(file_len2, counter2, cur_len2, block2, file2);
        }
    }

    delete []block1;
    delete []block2;
    delete []output_block;
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
//    read_and_print("output_sorted.bin");
    read_and_sort("input.bin");

    merge_all();
//    read_and_print("output.bin");
//    read_and_print("0");

//    read_and_print("0");
//    read_and_print("1");
//    read_and_print("2");
//    read_and_print("3");
//    read_and_print("4");
//    read_and_print("5");

}
