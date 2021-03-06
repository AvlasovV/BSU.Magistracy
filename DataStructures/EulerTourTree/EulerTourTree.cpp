/**
Дано дерево T. Выведите любой его эйлеров обход.

Эйлеровым обходом называется последовательность посещения вершин дерева при одном из обходов в глубину, но при этом вершина может выписываться несколько раз: в момент входа в нее и каждый раз, когда вы в нее возвращаетесь.

Формат входных данных
Первая строка входных данных содержит одно число n (2 ≤ n ≤ 100 000) — количество вершин в дереве.
Каждая из следующих n − 1 строк содержит по два числа ai, bi (1 ≤ ai, bi ≤ n, ai ≠ bi) — ребра дерева.

Гарантируется, что во входных данных дано дерево.

Формат выходных данных
Выведите 2 ⋅ n − 1 число — эйлеров обход дерева.
Примеры
стандартный ввод
5
1 2
2 3
3 4
4 5

стандартный вывод
1 2 3 4 5 4 3 2 1

стандартный ввод
2
1 2
стандартный вывод
1 2 1
*/


#include <iostream>
#include <vector>
#include <stack>
#include <fstream>

using namespace std;


struct Node {
	vector <int> edges;
	bool used = false;
	int number;
	int first_in = -1;
};

void dfs(vector <Node> &graph)
{
	stack <Node> eulerTour;
	eulerTour.push(graph[0]);
	while (!eulerTour.empty()) {

		Node cur_node = eulerTour.top();
		bool findUnusedNode = false;
		cout << cur_node.number + 1 << " ";
		for (int i = 0; i < cur_node.edges.size(); i++) {
			if ((graph[cur_node.edges[i]].used == false) && (cur_node.first_in != graph[cur_node.edges[i]].number)) {
				if (graph[cur_node.edges[i]].first_in == -1) {
					graph[cur_node.edges[i]].first_in = cur_node.number;
				}
				eulerTour.push(graph[cur_node.edges[i]]);
				//cout << cur_node.edges[i] + 1 << " ";
				findUnusedNode = true;
				break;
			}
		}

		if (!findUnusedNode) {
			graph[cur_node.number].used = true;
			eulerTour.pop();
			//cout << cur_node.number + 1 << " ";
		}
	}
}


int main()
{
	ifstream file_in("euler.in");
	int n;

	cin >> n;
	//file_in >> n;

	vector < Node > graph(n);

	//vector<bool> used;

	int a, b;
	//used.push_back(false);



	for (int i = 0; i < n - 1; i++) {
		//file_in >> a >> b;
		cin >> a >> b;

		graph[a - 1].edges.push_back(b - 1);
		graph[a - 1].number = a - 1;
		graph[b - 1].edges.push_back(a - 1);
		graph[b - 1].number = b - 1;
	}
	file_in.close();
	//cout << endl;
	//for (int i = 0; i < graph.size(); i++) {
	//	cout << i << ": ";
	//	for (int j = 0; j < graph[i].edges.size(); j++) {
	//		cout << graph[i].edges[j] << " ";
	//	}
	//	cout << "Number: "<< graph[i].number << " Flag: "<< graph[i].used << endl;
	//}

	//cout << endl;
	//cout << endl;
	dfs(graph);
	//cout << endl;
	//cout << endl;
}
