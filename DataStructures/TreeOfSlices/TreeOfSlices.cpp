/**
Big thanks for http://e-maxx.ru/algo/segment_tree
Cool source!

Задан массив A из n положительных чисел ai (1≤ai≤10^9). Необходимо уметь выполнять 4 вида запросов:

1 p v — присвоить p-му элементу массива значение v.
2 l r (l≤r) — прибавить единицу ко всем числам на отрезке [l..r].
3 l r (l≤r) — найти сумму четных чисел на отрезке [l..r].
4 l r (l≤r) — найти сумму нечетных чисел на отрезке [l..r].
Входные данные
Первая строка входных данных содержит два числа n и q (1≤n,q≤10^5) — размер массива и количество запросов.

Каждая из следующий q строк - запрос одного из 4 описанных выше видов.

Выходные данные
Для каждого запроса 3 и 4 вида выведите одно число — ответ на запрос.

Примеры
входные данные
4 9
1 2 3 4
3 1 4
2 1 3
4 1 4
3 1 4
1 4 10
3 1 3
3 2 4
4 1 3
4 2 4
выходные данные
6
3
10
6
14
3
3
входные данные
5 2
1 2 3 4 5
3 1 5
4 1 5
выходные данные
6
9
*/


#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;

struct Operations {
	int number;
	int l;
	int r;
};

struct Node{
    ll even_sum = 0; //чётные
    ll odd_sum = 0;  //нечётные

    int even_count = 0;
    int odd_count = 0;

    int value = -1;

    void print_node(){
        cout << "Value=" << this -> value << "\nEven/odd count:" << this -> even_count << ", " << this->odd_count << " Even/odd sums:" << this->even_sum << ", " << this->odd_sum << endl;
    }
};

void read_from_file(string filename, int &n, int &q, vector<ll> &arr, vector<Operations> &operations){
    ifstream file;
    file.open(filename);
    file >> n >> q;

    arr.reserve(n + 1);
    ll buf;
    for(int i = 0; i < n; i++){
        file >> buf;
        arr.push_back(buf);
    }

    operations.reserve(q);
    Operations buf_operation;
    for (int i = 0; i < q; i++){
        file >> buf_operation.number >> buf_operation.l >> buf_operation.r;
        operations.push_back(buf_operation);
    }
    file.close();
}


void build(vector<Node> &tree, vector<ll> arr, int v, int tleft, int tright) {

	if (tleft == tright){
		tree[v].value = arr[tleft];
		if (tree[v].value % 2 == 0){
            tree[v].even_sum = tree[v].value;
            tree[v].even_count = 1;
		}
		else{
            tree[v].odd_sum = tree[v].value;
            tree[v].odd_count = 1;
		}
	}
	else {
		int tm = (tleft + tright) / 2;

		build(tree, arr, v * 2, tleft, tm);
		build(tree, arr, v * 2 + 1, tm + 1, tright);

		tree[v].even_sum = tree[v * 2].even_sum + tree[v * 2 + 1].even_sum;
		tree[v].odd_sum = tree[v * 2].odd_sum + tree[v * 2 + 1].odd_sum;

		tree[v].even_count = tree[v * 2].even_count + tree[v * 2 + 1].even_count;
		tree[v].odd_count = tree[v * 2].odd_count + tree[v * 2 + 1].odd_count;
	}

}


//void update(vector<Node> &tree, int v, int tleft, int tright, int l, int r, int add) {
//	if (l > r)
//		return;
//	if (l == tleft && tright == r)
//		tree[v] += add;
//	else {
//		int tm = (tleft + tright) / 2;
//		update(tree, v * 2, tleft, tm, l, min(r, tm), add);
//		update(tree, v * 2 + 1, tm + 1, tright, max(l, tm + 1), r, add);
//	}
//}

ll get_even_sum(vector<Node> &tree, int v, int tleft, int tright, int l, int r){
    if (l > r)
		return 0;
	if (l == tleft && r == tright)
		return tree[v].even_sum;
	int tm = (tleft + tright) / 2;
	return get_even_sum (tree, v*2, tleft, tm, l, min(r,tm))
		+ get_even_sum (tree, v*2+1, tm+1, tright, max(l,tm+1), r);
}

ll get_odd_sum(vector<Node> &tree, int v, int tleft, int tright, int l, int r){
    if (l > r)
		return 0;
	if (l == tleft && r == tright)
		return tree[v].odd_sum;
	int tm = (tleft + tright) / 2;
	return get_odd_sum (tree, v*2, tleft, tm, l, min(r,tm))
		+ get_odd_sum (tree, v*2+1, tm+1, tright, max(l,tm+1), r);
}

void set_new_value(vector<Node> &tree, int v, int tleft, int tright, int pos, int new_val) {
	if (tleft == tright){
		tree[v].value = new_val;
		if (tree[v].value % 2 == 0){
            tree[v].even_sum = tree[v].value;
            tree[v].odd_sum = 0;
            tree[v].even_count = 1;
            tree[v].odd_count = 0;
		}
		else{
            tree[v].odd_sum = tree[v].value;
            tree[v].even_sum = 0;
            tree[v].odd_count = 1;
            tree[v].even_count = 0;
		}
	}
	else {
		int tm = (tleft + tright) / 2;
		if (pos <= tm)
			set_new_value(tree, v * 2, tleft, tm, pos, new_val);
		else
			set_new_value(tree, v * 2 + 1, tm + 1, tright, pos, new_val);

		tree[v].even_sum = tree[v * 2].even_sum + tree[v * 2 + 1].even_sum;
		tree[v].odd_sum = tree[v * 2].odd_sum + tree[v * 2 + 1].odd_sum;

		tree[v].even_count = tree[v * 2].even_count + tree[v * 2 + 1].even_count;
		tree[v].odd_count = tree[v * 2].odd_count + tree[v * 2 + 1].odd_count;
	}
}

int get(int tree[], int v, int tleft, int tright, int pos) {
	if (tleft == tright)
		return tree[v];
	int tm = (tleft + tright) / 2;
	if (pos <= tm)
		return tree[v] + get(tree, v * 2, tleft, tm, pos);
	else
		return tree[v] + get(tree, v * 2 + 1, tm + 1, tright, pos);
}

void print_vector(vector<ll> arr){
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void print_node_vector(vector<Node> tree){
    for(int i = 0; i < tree.size(); i++){
        tree[i].print_node();
        cout << endl;
    }
}

int main()
{
    int n, q;

    vector<ll> arr;
    vector<Operations> operations;

    read_from_file("1.txt", n, q, arr, operations);

    cout << "Operations\n";
    for(int i = 0; i < q; i++){
        cout << operations[i].number << " " << operations[i].l << " " << operations[i].r << endl;
    }

    cout << "Values\n";
    print_vector(arr);

    vector<Node> tree(4*n + 1);
    build(tree, arr, 1, 0 , n - 1);
    print_node_vector(tree);
    cout << get_even_sum(tree, 1, 0, n-1, 1, 4) << endl;
    set_new_value(tree, 1, 0, n-1, 4, 15);
    cout << get_even_sum(tree, 1, 0, n-1, 1, 4) << endl;
    cout << get_odd_sum(tree, 1, 0, n-1, 1, 4) << endl;


    print_node_vector(tree);




	/*for (int i = 0; i < q; ++) {
		cin >> operations[i].number >> operations[i].l >> operations[i].r;
	}*/


}
