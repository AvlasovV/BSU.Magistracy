/**
Дан массив A из n элементов. Необходимо обработать q запросов, i-й из которых задаётся числами li, ri, xi и yi. 
Ответом на i-й запрос является число элементов массива с индексами из отрезка [li, ri], которые не меньше xi и не больше yi.

Формат входных данных
Первая строка содержит два натуральных числа n и q (1 ≤ n, q ≤ 2 ⋅ 10^5) — размер массива и число запросов соответственно.
Вторая строка содержит n чисел ai (1 ≤ ai ≤ 10^9) — элементы массива A.

Далее следует q строк, каждая содержит по 4 числа. В i-й строке расположены четыре числа li, ri, xi, yi (1 ≤ li ≤ ri ≤ n, 1 ≤ xi ≤ yi ≤ 109).

Формат выходных данных
Выведите q строк — ответы на запросы.
Примеры
стандартный ввод
5 3
1 2 3 4 5
1 5 1 5
1 5 2 100
2 5 1 3
стандартный вывод
5
4
2
стандартный ввод
10 12
3 2 15 2 15 6 14 14 3 6
1 6 2 5
8 10 2 6
7 10 2 6
5 9 4 8
7 7 5 6
5 8 2 3
2 4 2 15
3 4 2 5
6 9 2 5
4 10 2 7
6 9 5 5
6 6 3 7
стандартный вывод
3
2
2
1
0
0
3
1
1
4
0
1
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;


struct Query {
	int left, right, x, y;
};
void print_query(Query q) {
	cout << q.left << " " << q.right << " " << q.x << " " << q.y;
}

struct Version {
	int max_value = 0;
	int count_of_nodes = 0;
};
struct Node {
	vector<Version> versions; 
	int left, right;
};

struct Leaf {
	int value;
	int position;
};

bool compare_leafs(Leaf a, Leaf b) {
	return a.value < b.value;
}

void print_leaf(vector<Leaf> l) {
	cout << "Position in original sequence: " << "   Value:" << endl;
	for (int i = 0; i < l.size(); i++) {
		cout << l[i].position << "    " << l[i].value << endl;
	}
}


void create_slice_tree(vector<Node> tree, vector<Leaf> values) {
	
	for (int i = 0; i < values.size(); i++) {
		bool is_exist = false;
		for (int j = 0; j < tree[0].versions.size(); j++) {
			if (tree[0].versions[j].max_value == values[i].value) {
				is_exist = true;
				tree[0].versions[j].count_of_nodes++;

				break;
			}
		}
		if (!is_exist) {
			Version vers;
			vers.max_value = values[i].value;
			tree[0].versions.push_back()
		}
	}
}


int main() {
	int n, q;
	ifstream input_file("input2.txt");

	input_file >> n >> q;
	vector<Leaf> values;
	vector<Node> tree;
	vector<Query> queries;
	Leaf buf;
	for (int i = 0; i < n; i++) {
		input_file >> buf.value;
		buf.position = i;
		values.push_back(buf);
	}
	Query buf_q;
	for (int i = 0; i < q; i++) {
		input_file >> buf_q.left >> buf_q.right >> buf_q.x >> buf_q.y;
		queries.push_back(buf_q);
	}
	input_file.close();

	sort(values.begin(), values.end(), compare_leafs);
	print_leaf(values);
	cin.get();

	for()

}