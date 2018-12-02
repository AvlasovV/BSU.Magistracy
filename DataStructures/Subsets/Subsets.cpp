/**
Вам даны два множества чисел: {a1, a2, …, an} и {b1, b2, …, bn}.

Среди всех возможных наборов из k различных индексов от 1 до n выберите тот,
при котором максимально отношение

(Ai1 + Ai2 + ... + Aik) / (Bi1 + ... + Bik)).

Формат входных данных
В первой строке входных данных дано одно целое число T (1≤ T ≤500),
количество тестовых наборов в файле.
Далее следуют T тестовых наборов. Каждый из них состоит из трех строк.

В первой строке записаны два целых числа n и k (1≤k≤n≤500).
Во второй строке записаны n целых чисел ai (1≤ai≤10^6).
В третьей строке записаны n целых чисел bi (1≤bi≤10^6).

Формат выходных данных
Для каждого тестового набора выведите k различных индексов от 1 до n.
Если существует несколько оптимальных наборов индексов, то выведите любой из них.

Пример
стандартный ввод
10
10 6
9 6 7 6 1 10 10 9 5 3
9 2 10 7 5 9 10 5 10 8
10 7
4 7 6 1 2 7 3 9 7 7
9 2 4 9 6 6 7 5 9 9
10 7
3 4 10 1 3 9 1 2 6 6
5 4 7 8 7 5 5 5 8 3
10 4
2 4 4 9 2 6 3 10 10 6
9 10 8 4 3 2 5 5 4 7
10 9
8 7 6 3 2 10 6 2 4 6
7 1 9 7 4 4 6 9 7 4
10 7
3 10 7 1 10 1 8 5 1 5
1 10 10 1 6 7 3 9 6 5
10 2
4 9 5 7 9 2 8 3 4 3
6 1 7 4 2 4 1 8 9 7
10 6
10 8 1 3 7 6 1 4 10 6
1 2 1 5 7 2 5 4 7 8
10 5
9 10 6 9 10 6 7 7 7 7
8 8 9 3 9 7 1 5 3 6
10 10
8 3 7 2 8 5 6 10 6 4
6 10 3 10 1 1 10 6 5 2

вывод:
1 2 4 6 7 8
2 3 5 6 8 9 10
1 2 3 6 8 9 10
4 6 8 9
1 2 3 4 5 6 7 9 10
1 2 3 4 5 7 10
2 7
1 2 3 6 8 9
4 7 8 9 10
1 2 3 4 5 6 7 8 9 10
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

struct Pair{
    int a, b, index;
    double proportion;
};
struct Value{
    double value;
    int index;
};

void read_from_file(int &T, vector<int> &n, vector<int> &k, vector < vector <Pair> > &pairs){

    ifstream input_file;
    int buf;
    input_file.open("input.txt");
    input_file >> T;
    Pair pair_buf;
    for (int i = 0; i < T; i++){

        input_file >> buf;
        n.push_back(buf);
        input_file >> buf;
        k.push_back(buf);

        vector<Pair> buf1;
        pairs.push_back(buf1);

        for(int j = 0; j < n[i]; j++){
            input_file >> pair_buf.a;
            pairs[i].push_back(pair_buf);
        }
        for(int j = 0; j < n[i]; j++){
            input_file >> buf;
            pairs[i][j].b = buf;
            pairs[i][j].index = j;
            pairs[i][j].proportion = (double)pairs[i][j].a / pairs[i][j].b;
        }
    }
    input_file.close();
}

void read_from_console(int &T, vector<int> &n, vector<int> &k, vector < vector <Pair> > &pairs){
    int buf;
    cin >> T;
    Pair pair_buf;
    for (int i = 0; i < T; i++){

        cin >> buf;
        n.push_back(buf);
        cin >> buf;
        k.push_back(buf);

        vector<Pair> buf1;
        pairs.push_back(buf1);

        for(int j = 0; j < n[i]; j++){
            cin >> pair_buf.a;
            pairs[i].push_back(pair_buf);
        }
        for(int j = 0; j < n[i]; j++){
            cin >> buf;
            pairs[i][j].b = buf;
            pairs[i][j].index = j;
            pairs[i][j].proportion = (double)pairs[i][j].a / pairs[i][j].b;
        }
    }
}

void print_vector(vector<int> values){
    for(int i = 0; i < values.size(); i++){
        cout << values[i] << " ";
    }
 }
void print_array(int * n, int length){
     for(int i = 0; i < length; i++){
        cout << n[i] << " ";
     }
 }

void print_pairs(vector<Pair> pairs){
     for(int i = 0; i < pairs.size(); i++){
        cout <<"Index:" << pairs[i].index << " and a, b, proportion: " << pairs[i].a << " " << pairs[i].b << " " << pairs[i].proportion << endl;
     }
 }

bool compare_pairs(Pair &x, Pair &y){
     if (x.proportion > y.proportion){
        return true;
     }
     else{
        return false;
     }
 }
bool compare_values(Value &x, Value &y){
     if (x.value > y.value){
        return true;
     }
     else{
        return false;
     }
 }

bool compare_values_by_index(Value &x, Value &y){
    if (x.index < y.index){
        return true;
     }
     else{
        return false;
     }
}

vector<Value> searching_best_indexes(vector<Pair> &pairs, double _z, int k){
    vector<Value> values;
    Value buf;
    double sum;
    for(int i = 0; i < pairs.size(); i++){
        buf.value = pairs[i].a - pairs[i].b * _z;
        buf.index = pairs[i].index;
        values.push_back(buf);
    }
    sort(values.begin(), values.end(), compare_values);
    return values;
}

vector<Value> binary_search(vector<Pair> &pairs, double z, int k){
    vector<Value> values;
    double right = 0;
    double left = z + 1;
    double sum, midd;

    while (1) {
            if (left - right < 1e-8){
                return values;
            }
            midd = (left + right) / 2;

            values = searching_best_indexes(pairs, midd, k);
            sum = 0;
            for(int i = 0; i < k; i++){
                sum += values[i].value;
            }

            if(sum == 0){
                return values;
            }
            if (sum < 0){
                left = midd;
            }
            if(sum > 0){
                right = midd;
            }
        }
}

void find_sequence(vector<Pair> pairs, int k){
    sort(pairs.begin(), pairs.end(), compare_pairs); // maybe here we can not sort but just find max proportion ( O(n) < O(n * log(n) )
    double z = pairs[0].proportion;

    vector<Value> values;
    values = binary_search(pairs, z, k);
    sort(values.begin(), values.begin() + k, compare_values_by_index);
    for(int i = 0; i < k; i++){
        cout << values[i].index + 1 << " ";
    }
    cout << endl;
}

int main(){
    int T;
//    cin >> T;
    int buf;
    vector <int> n, k;
    vector < vector <Pair> > pairs;
    //read_from_file(T, n, k, pairs);
    read_from_console(T, n, k, pairs);
    //print_array(n, T);
//    print_pairs(pairs[0]);
//    sort(pairs[0].begin(), pairs[0].end(), compare_pairs);
//    cout << endl << endl;
//    print_pairs(pairs[0]);
//    cout <<1e-8<<endl;
    for(int i = 0; i < T; i++){
        find_sequence(pairs[i], k[i]);
    }
//    for (int i = 0; i < T; i++){
//        cin >> n[i] >> k[i];
//        for(int j = 0; j < n[i]; j++){
//            cin >> buf;
//            a[i].append(buf);
//        }
//        for(int j = 0; j < n[i]; j++){
//            cin >> buf;
//            b[i].append(buf);
//        }
//    }
//


}
