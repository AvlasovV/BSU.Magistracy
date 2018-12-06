/**
В данной задаче необходимо реализовать фильтр Блума.


Операции (аргументы строковые величины):

insert — вставка элемента;
contains — проверка, правда ли элемент был добавлен ранее.

При запросе contains требуется, если элемент на самом деле был ранее добавлен, возвращать «да» во всех случаях,
а если элемент на самом деле добавлен не был, то возвращать «нет» хотя бы в 99% случаев.

Input
В первой строке записано число N запросов к фильтру (10000≤N≤1000000).
Далее каждая из N последующих строк состоит из двух элементов: тип запроса и значение запроса, разделённые пробелом.
Тип запроса может принимать значение 0 или 1.
Если тип равен 1, то значение запроса — объект, который необходимо добавить в фильтр, а если тип равен 0 — объект, для которого необходимо проверить, был ли он добавлен ранее.
Значение запроса — строка длины от 1 до 25, состоящая из больших и малых букв английского алфавита и цифр.
Гарантируется, что запросов insert будет не более 600000, при этом запросов contains с ответом «нет» хотя бы 10000.

Output
Выходной файл состоит из одной строки, содержащей ответы на все запросы contains в порядке их следования.
Каждый из ответов представлен единственным символом: 0, если ответ «нет», или 1, если «да».
Example
input.txt
3
1 foo
0 foo
0 bar

output.txt
10
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#include <string>
#include <functional>
#include <cstring>
#include <stdlib.h>
#include <cmath>

using namespace std;


class BloomFilter{

private:
    hash<string> hash1;
    long long bit_length;
    int k; // count of hash-functions
    double probability_of_error;
    vector<bool> filter_array;

public:
    long long hash2(string data);
    BloomFilter(int length_of_input_data, double probability_of_error);
    void add(string data);
    bool contain(string data);
    long long k_hash(string data);
};


int main(){

    ifstream input_file;
    input_file.open("input.txt");

    ofstream output_file;
    output_file.open("output.txt");

    int N;
    int check;
    string sbuf;
//    vector<bool> contain;

    input_file >> N;
    BloomFilter bloom(min(N, 600000), 0.01);

    for(int i = 0; i < N; i++){
        input_file >> check >> sbuf;
        if(check){
            bloom.add(sbuf);
        }
        else{
//            contain.push_back(bloom.contain(sbuf));
            output_file << bloom.contain(sbuf);
        }
    }

    input_file.close();

//    ofstream output_file;
//    output_file.open("output.txt");
//    for (const auto &e : contain) output_file << e;
    output_file.close();

}


BloomFilter::BloomFilter(int length_of_input_data, double probability_of_error): probability_of_error(probability_of_error){
//    this.probability_of_error = probability_of_error;
    this -> bit_length = -(length_of_input_data) * log(probability_of_error) / (log(2) * log(2));
    filter_array.resize(bit_length);
    this -> k = (this -> bit_length / length_of_input_data) * log(2);
}


void BloomFilter::add(string data){

    long long position;
    for (int i = 0; i < k; i++){
        position = (hash1(data)+ i * hash2(data)) % bit_length;
        filter_array[position] = true;
    }
}

bool BloomFilter::contain(string data){

    long long position;
    long long hash1_buf = hash1(data), hash2_buf = hash2(data);

    for (int i = 0; i < k; i++){
        position = (hash1_buf + i * hash2_buf) % bit_length;
        if(!filter_array[position]){
            return false;
        }
    }
    return true;
}

long long BloomFilter::hash2(string data)
{
//   int seed = 131;
//   unsigned long hash = 0;
//   for(int i = 0; i < data.length(); i++)
//   {
//      hash = (hash * seed) + data[i];
//   }
//   return hash % bit_length;

// more simple hash
    long long sum = 0;
    for (int k = 0; k < data.length(); k++)
        sum = sum + int(data[k]);
    return  sum % bit_length;

}
















