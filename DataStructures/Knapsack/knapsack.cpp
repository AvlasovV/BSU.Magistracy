/**
 Дано n предметов, каждый из них характеризуется весом и ценностью.

Необходимо собрать рюкзак весом не больше W такой, что суммарная ценность всех вещей в рюкзаке будет максимально возможной. Другими словами, необходимо выбрать подмножество предметов с ограничением на суммарную массу с максимальной ценностью.

Входные данные
Первая строка входных данных содержит два числа n (1 ≤ n ≤ 40) и W (1 ≤ W ≤ 109) — количество предметов и максимальный вес, который можно нести в рюкзаке.

Каждая из следующих n строк содержит по два числа wi и pi (1 ≤ wi, pi ≤ 109) — вес предмета и его ценность.

Выходные данные
В первой строке выведите одно число k (0 ≤ k ≤ n) — количество предметов, которые составляют выбранное множество.

Во второй строке выведите различных k целых чисел от 1 до n, номера выбранных предметов. Предметы пронумерованы в порядке следования во входных данных.

Так как оптимальных решений может быть несколько, можете вывести любое из них.

Примеры
входные данные
5 10
1 1
2 2
3 3
4 4
5 5
выходные данные
3
1 4 5 
входные данные
13 2496
106 6026683
83 54704975
283 61225570
980 96186912
1 15136196
939 75210429
590 7271840
862 33796706
379 82719123
293 29363370
658 45670343
15 91375654
367 78847080
выходные данные
8
2 3 4 5 9 10 12 13 
 */

#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <valarray>

using namespace std;
typedef long long int ll; 

struct Item{
    ll weight;
    ll price;
    vector<int> indexes;
};

void get_sum(vector<Item> &arr, int * prices, int * weights, int n, int c) 
{ 
    for (int i = 0; i < (1 << n); i++) 
    { 
        ll price = 0;
        ll weight = 0;
        for (int j = 0; j < n; j++) 
            if (i & (1 << j)) {
                price += prices[j + c];
                weight += weights[j + c]; 
                arr[i].indexes.push_back(j + c + 1);
            }
        
        arr[i].weight = weight;
        arr[i].price = price;
    } 
} 


//void delete_bad_variants(vector<Item> &arr, vector<Item> &new_arr, ll W, int n){
void delete_bad_variants(vector<Item> &arr, ll W, int n){
    vector<Item> good_variants;
    
    ll max_price = -1;
    
    if(arr.size() > 0){
        max_price = arr[0].price;
        for (int i = 0; i < 1 << n; i++) {
            if (arr[i].weight > W){
                break;
            }
            if (max_price < arr[i].price){
                max_price = arr[i].price;
                good_variants.push_back(arr[i]);
            }
        }
        arr = good_variants;
    }
}



int binary_search(vector<Item> &arr, ll weight, ll W){
    
    int midd = 0;
    ll max_price = 0;
    int current_index = -1;
    
    if(arr.size() > 0){
        int left = 0;
        int right = arr.size() - 1;
        while (1) {
            if (left > right){
                return current_index;
            }
            midd = (left + right) / 2;
            if(weight + arr[midd].weight == W){
                return midd;
            }
            if (weight + arr[midd].weight < W){
                current_index = midd;
                left = midd + 1;
            }       
            if(weight + arr[midd].weight > W){
                right = midd - 1;
            }
        }
    }
    else {
        return current_index;
    }
}

void meet_in_the_middle(vector<Item> &first, vector<Item> &second, ll W){
    
    ll max_price = -1;
    int max_f = -1;
    int max_s = -1;
    
    int cur_f = -1;
    int cur_s = -1;
    ll current_price = -1;
    
    for(int i = 0; i < second.size(); i++){
        if(second[i].weight > W){
            continue;
        }
        cur_f = binary_search(first, second[i].weight, W);
        if(cur_f == -1){
            current_price = second[i].price;
        }
        else{
            current_price = second[i].price + first[cur_f].price;
        }
        if(max_price < current_price){
            max_f = cur_f;
            max_s = i;
            max_price = current_price;
        }
        
    }
    
    if(max_price >= 0){
        if(max_f == -1 && max_s == -1){
            cout << 0 << endl;
        }
        else if(max_f == -1){
            cout << second[max_s].indexes.size() << endl;
            for(int i = 0; i < second[max_s].indexes.size(); i++){
                cout << second[max_s].indexes[i] << ' ';
            }
        }
        else if (max_s == -1){
            cout << first[max_f].indexes.size() << endl;
            for(int i = 0; i < first[max_f].indexes.size(); i++){
                cout << first[max_f].indexes[i] << ' ';
            }
        }
        else{
            cout << first[max_f].indexes.size() + second[max_s].indexes.size()<< endl;
            for(int i = 0; i < first[max_f].indexes.size(); i++){
                cout << first[max_f].indexes[i] << ' ';
            }
            for(int i = 0; i < second[max_s].indexes.size(); i++){
                cout << second[max_s].indexes[i] << ' ';
            }
        }
        
    }
        
    
}


bool compare(const Item &i, const Item &j)
{
    return i.weight < j.weight;
}

int main() {
    int n;
    ll W;
    cin >> n >> W;
    int half_n = n / 2;
    int * weights = new int[n];
    int * prices = new int[n];
    for(int i = 0; i < n; i++){
        cin >> weights[i] >> prices[i];
    }
    
    vector<Item> first(1 << half_n);
//    vector<Item> good_subsets(1 << half_n);
    
//    vector<Item> good_subsets;
//    good_subsets.reserve(1 << half_n);
    
    get_sum(first, prices, weights, half_n, 0);
    
    
//    search_best(first, W, n/2);
//*************************************************************    
    
//    cout << "All combinations of first half:" << endl;
//    for (int i = 0; i < (1 << half_n); i++){ 
//        cout << first[i].weight << " " << first[i].price << endl;
//    }
//    
    
    sort(first.begin(), first.end(), compare);
    
//    cout << "Sorted:" << endl;
//    for (int i = 0; i < (1 << half_n); i++){ 
//        cout << first[i].weight << " " << first[i].price << endl;
//    }
    
    delete_bad_variants(first, W, half_n);
    
    
//    cout << "Now we sort and delete bad variants:" << endl;
//    for (int i = 0; i < first.size(); i++){ 
//        cout << first[i].weight << " " << first[i].price << " "; 
//        cout << "Indexes: ";
//        for(int j = 0; j < first[i].indexes.size(); j++){
//            cout << first[i].indexes[j] << " ";
//        }
//        cout << endl;
//    }
    
    vector<Item> second(1 << (n - half_n));
    get_sum(second, prices, weights, n - half_n, half_n);
    meet_in_the_middle(first, second, W);
    
    
//    cout << "Now we sort:" << endl;
//    
//    sort(first[0][0], first[1 << n/2][0]);
//    
//    for (int i = 0; i < (1 << half_n); i++) 
//    { 
//        for (int j = 0; j < 2; j++) {
//            cout << first[i][j] << " ";
//        }
//        cout << endl;
//    } 
    
    
    // cout <<"Enter n: ";
    // cin >> n;
    // cout << "Hello " << n;
    
}