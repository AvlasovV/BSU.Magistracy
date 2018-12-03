/**
Требуется реализовать алгоритм присоединения списка (Join) для последовательности переходов.
Входной список закольцован, т.е. можно полагать, что за последним элементом следует первый.

Input
Первые 4 байта входного файла задают число N элементов в списке, который нужно упорядочить (1≤N).
Следующие 8×N байт задают по два целых числа (i, nexti), что означает следование числа nexti за числом i.
Список состоит из различных целых положительных чисел, числа не превосходят 230.
Общий объем входного файла не превосходит 10000004 байт.

Output
Выведите результат также в бинарном формате. Вы должны вывести ровно 12×N байт.
В порядке возрастания элементов списка выведите тройки: i, nexti, next(nexti).

Example
input.bin
5 4 5 5 1 1 2 3 4 2 3
output.bin
1 2 3 2 3 4 3 4 5 4 5 1 5 1 2
Note
Пример в задаче приведён в текстовом формате для пояснения. Входной файл в бинарном формате.
Если ваше решение использует более 700 МБ, то места для создания дополнительных файлов может не хватить.
*/
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


struct Pair{
    int current;
    int next;
};

void write_sequence(vector<int> seq, char* filename){
    ofstream output_file;
    output_file.open(filename, ios::out | ios:: binary);
    int size = seq.size();
    output_file.write((char*)&(size), sizeof(int));
    Pair buf;
    for (int i = 0; i < seq.size() - 1; i++){
        buf.current = seq[i];
        buf.next = seq[i + 1];
        output_file.write((char*)&(buf.current), sizeof(int));
        output_file.write((char*)&(buf.next), sizeof(int));
    }
    output_file.write((char*)&seq[seq.size() - 1], sizeof(int));
    output_file.write((char*)&seq[0], sizeof(int));
    output_file.close();
}

int main(){


    vector<int> sequence;
    for(int i = 1; i < 11; i++){
        sequence.push_back(i);
        //sequence.push_back(i * 100000000 + i);
    }
    write_sequence(sequence,"output.bin");


    ifstream input_file;

//
    int N;
    vector<Pair> pairs;
    input_file.open("output.bin", ios::in | ios::binary);
    input_file.read((char*)&N, sizeof(int));
    cout << "N = " << N << endl;
    Pair buf;
    for(int i = 0; i < N; i++){
        input_file.read((char*)&buf.current, sizeof(int));
        input_file.read((char*)&buf.next, sizeof(int));
        pairs.push_back(buf);
    }
    for(int i = 0; i < pairs.size(); i++){
        cout << pairs[i].current << " " << pairs[i].next << endl;
    }
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
