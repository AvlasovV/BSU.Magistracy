/** 
Рассмотрим поток целых неотрицательных чисел S = (a1, a2, …, an) и некоторую целочисленную константу k.

Число x будем называть доминирующим в потоке, если оно встречается в S более чем n / k раз.

Прочитайте входной поток один раз и выведите кандидаты в тяжелые элементы. 
Помните, что все действительно доминирующие к этому моменту элементы должны быть выведены.

Формат входных данных
В первой строке входных данных содержится число k (2 ≤ k ≤ 1000).
Далее по одному числу в строке содержатся элементы потока S.

Входные данные заканчиваются числом −1. Каждый раз, когда вы считываете число 0, 
требуется вывести элементы, доминирующие на прочитанной части потока (число 0 не является элементом потока S).
Известно, что число элементов в S не превосходит 10^6. Все числа ai не превосходят 10^9. Число запросов (чисел 0) во входных данных не более 1000.

Формат выходных данных
Для каждого запроса доминирующих элементов выведите одну строку, содержащую ровно (k − 1) натуральных чисел (от 1 до 10^9). Среди этих чисел должны встречаться все доминирующие элементы.
Числа в строке могут повторяться.

Пример
стандартный ввод	
3 
1 1 1 0 2 2 2 0 3 3 3 0 2 3 3 3 3 3 3 3 3 3 0 -1
стандартный вывод
1 1
1 2
1 1
2 3
*/

#include <iostream>
#include <vector>
#include <map>

using namespace std;


struct Hitter {
	int value = -1;
	int frequency = 0;
};

int main() {
	int k;
	cin >> k;
	k--;
	Hitter * hitters = new Hitter[k];
	int empty_places = k;
	int empty_index = -1;
	//int val_buf = 1;
	//map<int, int> hitters1;


	int buf = 0;
	bool is_in = false;
	//bool found_place = false;
	cin >> buf;

	//while (buf >= 0) {
	//	if (buf > 0) {
	//		if (hitters1.find(buf) == hitters1.end()) {
	//			if (hitters1.size() < k) {
	//				hitters1.insert(make_pair(buf, 1));
	//			}
	//			else {
	//				for (auto & x : hitters1) {
	//					if (x.second <= 0) {
	//						hitters1.erase(x.first);
	//						hitters1.insert(make_pair(buf, 1));
	//						find_place = true;
	//						break;
	//					}
	//				}
	//				if (!find_place) {
	//					for (auto & x : hitters1) {
	//						x.second--;
	//					}
	//				}
	//			}
	//		}
	//		else {
	//			hitters1[buf]++;
	//		}
	//	}
	//	else {
	//		for (auto &const x : hitters1) {
	//			val_buf = x.first;
	//			cout << val_buf << " ";
	//		}
	//		if (hitters1.size() < k) {
	//			for (int i = 0; i < k - hitters1.size(); i++) {
	//				cout << val_buf << " ";
	//			}
	//		}
	//		cout << endl;
	//	}
	//	find_place = false;
	//	cin >> buf;
	//}

	while (buf >= 0) {

		if (buf > 0) {	

			empty_index = -1;
			is_in = false;

			for (int i = 0; i < k; i++) {
				
				if (hitters[i].value == buf) {
					hitters[i].frequency++;
					is_in = true;
					break;
				}
				
				if (hitters[i].frequency <= 0 && empty_index == -1) {
					/*hitters[i].value = buf;
					hitters[i].frequency = 1;
					found_place = true;
					break;*/
					empty_index = i;
				}
			}

			if (!is_in) {
				if (empty_index == -1) {
					for (int i = 0; i < k; i++) {
						hitters[i].frequency--;
					}
				}
				else {

					hitters[empty_index].value = buf;
					hitters[empty_index].frequency = 1;
					
					if (empty_places >= 1) {
						empty_places--;
					}
				}

			}

		}

		else {

			for (int i = 0; i < k - empty_places; i++){
				cout << hitters[i].value << " ";
			}

			for (int i = 0; i < empty_places; i++)
			{
				cout << hitters[0].value << " ";
			}
			cout << endl;
			
		}

		cin >> buf;
		//is_in = false;
		
	}

}