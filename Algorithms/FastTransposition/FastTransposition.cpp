/** 
В этой задаче вам потребуется выполнить несколько операций транспонирования квадратной подматрицы данной матрицы A. 
Матрицу A будет представлять линейным массивом d, т.е. Ai, j = di·n + j. Индексация строк и столбцов матрицы A начинается с 0.
Так как наша цель быстро выполнять именно операцию транспонирования, то входную матрицу нужно сгенерировать следующим генератором:
vector<int> generate_input(int n, int seed) {
	vector<int> d(n * n);
	for (size_t i = 0; i < d.size(); ++i) {
		d[i] = seed;
		seed = ((long long) seed * 197 + 2017) & 987654;
	}
	return d;
}
Кроме этого выводить в результате саму матрицу не требуется, а нужно вывести только результат работы следующей функции:
long long get_hash(const vector<int>& d) {
	const long long MOD = 987654321054321LL;
	const long long MUL = 179;

	long long result_value = 0;
	for (size_t i = 0; i < d.size(); ++i)
		result_value = (result_value * MUL + d[i]) & MOD;
	return result_value;
}
Входные данные
В первой строке входных данных записаны два целых числа n и seed (1 ≤ n, seed ≤ 10000).
Вторая строка содержит число k (1 ≤ k ≤ 10) — количество операций транспонирования.
Каждая из последующих k строк содержит описание подматрицы, 
которую нужно транспонировать: imin, jmin и side (0 ≤ imin, jmin < n, 1 ≤ size ≤ n - max{imin, jmin}).

Выходные данные
Выведите только результат вызова функции get_hash с параметром d равным результату транспонирования исходной матрицы k раз.

Примеры
входные данные
3 10
1
0 0 3
выходные данные
537985024

входные данные
3 1
3
0 0 3
0 1 2
1 0 2
выходные данные
5570561

входные данные
1111 111
1
11 1 111
выходные данные
985162958569569
*/

#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int BLOCK_SIZE = 1024;

struct MatrixSizeStruct {
	int min_i;
	int min_j;
	int size_i;
	int size_j;
	//MatrixSizeStruct() : min_i(0), min_j(0), size(0) {}
	MatrixSizeStruct(int i=0, int j=0, int size_i=0, int size_j=0) : min_i(i), min_j(j), size_i(size_i), size_j(size_j) {}
};

vector<int> generate_input(int n, int seed) {
	vector<int> d(n * n);
	for (size_t i = 0; i < d.size(); ++i) {
		d[i] = seed;
		seed = ((long long)seed * 197 + 2017) & 987654;
		//cout << i << " ";
	}
	//cout << "\nHave been generated";
	return d;
}

long long get_hash(const vector<int>& d) {
	const long long MOD = 987654321054321LL;
	const long long MUL = 179;

	long long result_value = 0;
	for (size_t i = 0; i < d.size(); ++i)
		result_value = (result_value * MUL + d[i]) & MOD;
	return result_value;
}


void print_vector_like_matrix(vector<int> v, MatrixSizeStruct m_size) {
	//cout << "\nPrint matrix:\n";
	for (int i = 0; i < m_size.size_i; i++) {
		for (int j = 0; j < m_size.size_j; j++) {
			cout << v[i * m_size.size_j + j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}


void transpose_block(vector<int> &a, MatrixSizeStruct &m_size) {
	
	if (m_size.size_i == m_size.size_j) {
		for (int i = 0; i < m_size.size_i; i++) {
			for (int j = 0; j < i; j++) {
				swap(a[i * m_size.size_i + j], a[j * m_size.size_i + i]);
				//transposed_m.push_back(a[m_size.size_j * i + j]);
			}
		}
	}
	else {
		vector<int> transposed_m;
		transposed_m.reserve(m_size.size_j + m_size.size_i);
		for (int j = 0; j < m_size.size_j; j++) {
			for (int i = 0; i < m_size.size_i; i++) {
				//swap(a[i * m_size.size_i + j], a[j * m_size.size_j + i]);
				transposed_m.push_back(a[m_size.size_j * i + j]);
			}
		}
		a = transposed_m;
	}

}

vector<int> extract_submatrix(vector<int> &a, MatrixSizeStruct &m, int &n) {
	
	vector<int> sub_m;
	
	//cout << "Extract sub matr:" << endl;
	
	for (int i = 0; i < m.size_i; i++) {
		for (int j = 0; j < m.size_j; j++) {
			
			//sub_m[i * m.size_i + j] = a[(i + m.min_i) * n + j + m.min_j];
			sub_m.push_back(a[(i + m.min_i) * n + (j + m.min_j)]);

			//cout << sub_m[sub_m.size() - 1] << " ";
	
		}
		
		//cout << endl;
	
	}
	return sub_m;
}

void integrate_submatrix(vector<int> &m, vector<int> &sub_m, MatrixSizeStruct sub_m_params, int n) {
	
	for (int i = 0; i < sub_m_params.size_i; i++) {

		for (int j = 0; j < sub_m_params.size_j; j++) {
			
			m[((i + sub_m_params.min_i) * n) + (j + sub_m_params.min_j)] = sub_m[i * sub_m_params.size_j + j];
		
		}
	}
	vector<int>().swap(sub_m);

}

void transpose(vector<int> &matrix, MatrixSizeStruct sub_m_size, int n) {
	
	MatrixSizeStruct pointer_sub_m = MatrixSizeStruct();
	MatrixSizeStruct sub_size1;
	MatrixSizeStruct sub_size2;

	vector<int> sub_m1, sub_m2;
	
	int block_length_i = 0;
	int block_length_j = 0;
	
	int counter = ceil((double)(sub_m_size.size_i) / BLOCK_SIZE);
	int offset = 0;

	//int cur_counter = counter;
	//bool flag = false;

	//while (pointer_sub_m.min_i + pointer_sub_m.min_j < 2 * (sub_m_size.size_i - 1)) {	
	
	while (counter > 0) {
		for (int k = 0; k < counter; k++) {

			if (pointer_sub_m.min_i >= sub_m_size.size_i) {
				//pointer_sub_m.min_i -= block_length_i;
				pointer_sub_m.min_i = offset;
				pointer_sub_m.min_j += block_length_j;
			}

			block_length_i = min(BLOCK_SIZE, sub_m_size.size_i - pointer_sub_m.min_i);
			block_length_j = min(BLOCK_SIZE, sub_m_size.size_j - pointer_sub_m.min_j);
			
			if (k == 0) {
				offset += block_length_i;
			}


			sub_size1 = MatrixSizeStruct(pointer_sub_m.min_i + sub_m_size.min_i,
				pointer_sub_m.min_j + sub_m_size.min_j, block_length_i, block_length_j);
			sub_size2 = MatrixSizeStruct(pointer_sub_m.min_j + sub_m_size.min_i,
				pointer_sub_m.min_i + sub_m_size.min_j, block_length_j, block_length_i);

			sub_m1 = extract_submatrix(matrix, sub_size1, n);
			transpose_block(sub_m1, sub_size1);

			//print_vector_like_matrix(sub_m1, sub_size2);

			if (pointer_sub_m.min_i != pointer_sub_m.min_j) {


				sub_m2 = extract_submatrix(matrix, sub_size2, n);
				transpose_block(sub_m2, sub_size2);


				//print_vector_like_matrix(sub_m2, sub_size1);

				integrate_submatrix(matrix, sub_m1, sub_size2, n);
				integrate_submatrix(matrix, sub_m2, sub_size1, n);

			}
			else {
				integrate_submatrix(matrix, sub_m1, sub_size2, n);
				//integrate_submatrix(sub_m1);
			}

			pointer_sub_m.min_i += block_length_i;
			//flag = false;
			//pointer.min_j += block_length_j;


		}
		counter--;
		//cout << "End of transpose";
	}
	
}





int main()
{
	int n, seed;
	cin >> n >> seed;
	int k;
	cin >> k;
	MatrixSizeStruct* submatrix = new MatrixSizeStruct[k];
	for (int i = 0; i < k; i++) {
		cin >> submatrix[i].min_i >> submatrix[i].min_j >> submatrix[i].size_i;
		submatrix[i].size_j = submatrix[i].size_i;
	} 

	vector<int> result_matrix = generate_input(n, seed);

	for (int i = 0; i < k; i++) {
		transpose(result_matrix, submatrix[i], n);
		//cout << "hi\n";
		//sub_m = extract_submatrix(result_matrix, submatrix[i], n);
		//transpose(sub_m, submatrix[i].size);
		////print_vector_like_matrix(sub_m, m_size.size);
		//integrate_submatrix(result_matrix, sub_m, submatrix[i], n);
		
		/*vector<int>().swap(sub_m); 
		*/
		//sub_m.clear();
	}
	cout << get_hash(result_matrix);

	//int n = 4;
	//vector<int> original (n * n);
	//for (int i = 0; i < n * n; i++) {
	//	original[i] = i + 1;
	//}

	//MatrixSizeStruct m_size = MatrixSizeStruct();
	//m_size.size_i = m_size.size_j = n;

	//print_vector_like_matrix(original, m_size);
	//cout << endl;
	//
	//vector<int> test = original;

	//MatrixSizeStruct sub_m_size = MatrixSizeStruct(0, 0, 4, 4);
	////MatrixSizeStruct MatrixSizeStruct = matrixsizestruct(1, 1, 3, 3);


	//transpose_block(test, sub_m_size);
	////transpose(test, sub_m_size, n);
	//print_vector_like_matrix(test, m_size);

	//test = original;
	//sub_m_size = MatrixSizeStruct(0, 1, 3, 3);
	//transpose(test, sub_m_size, 4);
	//print_vector_like_matrix(test, m_size);
	
	return 0;
}