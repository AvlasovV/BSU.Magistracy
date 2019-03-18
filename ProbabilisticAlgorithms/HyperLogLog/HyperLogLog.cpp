/**
Задача 16. Уникальные пользователи
Имя входного файла: стандартный ввод
Имя выходного файла: стандартный вывод
Ограничение по времени: 5 с
Ограничение по памяти: 1 МБ
Денис хочет приблизительно подсчитать число уникальных посетителей тестирующей системы https://acm.bsu.by/,
используя не более 1 мегабайта памяти. Помогите ему сделать это. Гарантируется, что число уникальных посетителей не превосходит 500 тысяч.

Формат входного файла
На стандартных ввод поступает лог-файл идентификаторов посетителей сайта за последний месяц. 
Идентификаторы в файле могут повторяться. Каждая строка содержит буквенно-цифровой идентификатор пользователя сайта (не больше 10 символов) и только его. 
Число строк в файле не превосходит 2 миллионов.
Формат выходных данных
Выведите ровно одно целое число — приблизительное число уникальных пользователей за последний месяц. Допустимая относительная погрешность ответа составляет 1,5 %.
Пример
стандартный ввод	
id1
id2
id3
...
id22999
стандартный вывод
22927
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;


int k = 18; 					// First left bits, affects accuracy
int m = pow(2, k); 				// count of cells in our Hyper LogLog

double a = 0.7213 / (1 + 1.079 / m); 		// Constant with complex mathematical justification

unsigned int fnv1a(string text)
{
	/** Fast 32-bit hash function */
	int hash = 2166136261;
	vector<char> cstr(text.c_str(), text.c_str() + text.size() + 1);
	for (int i = 0; i < cstr.size(); ++i)
	{
		hash ^= cstr[i];
		hash += (hash << 1) + (hash << 4) + (hash << 7) + (hash << 8) + (hash << 24);
	}
	hash = (unsigned int)hash >> 0;
	return hash;
}

int main() {
	
	vector<unsigned short> values(m, 0);	// Our cells
	string temp;
	unsigned int hash_val = 0;
	unsigned int index = 0;
	unsigned int value = 0;
	unsigned short res = 0;
	
	// Here we getting stream and calculate unique values
	while (getline(cin, temp)) {		
		if (temp.compare("") == 0) {
			break;
		}
		
		hash_val = fnv1a(temp);
		index = hash_val >> (32 - k);		// Getting index of cell, first k bits
		value = hash_val & ((1 << 32 - k) - 1);	// Getting value, last (32 - k) bits
		res = (32 - k) - (int)log2(value);	// Getting cell value, first non-zero bit in value
		values[index] = (values[index] < res) ? res : values[index];
	}

	// For test, just all unique values
	
	//for (int i = 0; i < 10000; i++)
	// {
	//	hash_val = fnv1a(to_string(i));
	//	index = hash_val >> (32 - k);
	//	value = hash_val & ((1 << 32 - k) - 1);
	//	res = (32 - k) - (int)log2(value);
	//	values[index] = (values[index] < res) ? res : values[index];
	//}


	// Calculating and fixing estimate. To understand why it works like it works you need to read article: 
	// http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf 
	double estimate = 0;
	int empty_cells = 0;

	for (int i = 0; i < values.size(); ++i) {
		estimate += pow(2, -values[i]);
		if (values[i] == 0)
			empty_cells++;
	}
	estimate = 1. / estimate;
	estimate = estimate * a * pow(m, 2);

	//cout << "Raw estimate = " << estimate << endl;

	// Fix small estimates
	if ((estimate < (2.5 * m)) && (empty_cells > 0)) {
		estimate = m * log((double)m / empty_cells);
	}
	// Fix big estimates
	else if (estimate > (1. / 30) * UINT32_MAX) {
		estimate = -(UINT32_MAX * (1. - estimate / UINT32_MAX));
	}

	//cout << "Estimate = " << estimate << endl;
	cout << (int)estimate << endl;

	cin.get();
}
