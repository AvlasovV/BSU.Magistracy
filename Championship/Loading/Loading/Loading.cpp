/**
Ales is an active internet user. Today he started downloading several big files, 
and he knows an estimated download time for each of these files. 
However, this time is obviously incorrect due to the following reason. 
When some file is loaded successfully, the speed of downloading of all other files will be increased,
because the internet channel is divided equally between all active downloads. 
Therefore Ales has a reasonable question: when will he get all the files? Please help him to find an answer to this question.

Формат входных данных
The first line contains the number n of files (0 ≤ n ≤ 200 000). The second line contains n positive integers less than 10^9, the estimated time for each file.
Формат выходных данных
Output one real number, the answer to Ales’s question. The absolute or relative error shouldn’t exceed 10−9.
Примеры
loading.in	loading.out
5
1 2 3 4 5
3.0000000000000

3
13 21 34
22.6666666666667

2
5 5
5.0000000000000


!!!! We should hust think about average of all times:

	Scope_of_work = Sum_of_all(t_i) * (Absolute_speed / n)
	time = Scope_of_work / Absolute_speed =  Sum_of_all(t_i) / n
*/

#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ifstream file_in("loading.in");
	double n, buf;
	file_in >> n;
	vector <double> times(n);
	for (int i = 0; i < n; i++) {
		file_in >> buf;
		times[i] = buf;
	}
	file_in.close();
	//sort(times.begin(), times.end());
	//for (auto i : times) {
	//	cout << i << " ";
	//}


	double time = 0.;
	double time_left = 0;
	double previous_time = 0;
	int i = 0;
	int count_of_same_files = 1;
	double cur_factor = 1.;
	double global_factor = 1.;
	double cur_sum = 0;
	vector <double> operations;

	for (int j = 0; j < n; j++) {
		cur_sum += times[j];
	}
	if (n > 0) {
		time = cur_sum / n;
	}
	//while (i < n) {
	//	
	//	//time_left = (times[i] - previous_time);

	//	while (i + count_of_same_files < n) {
	//		if (!(times[i] == times[i + count_of_same_files])) {
	//			break;
	//		}
	//		count_of_same_files++;
	//	}
	//	
	//	double m1 = n - i - count_of_same_files;
	//	double m2 = n - i;
	//	//cur_factor = cur_factor * ((n - cur_index - count_of_same_files) / (n - cur_index));
	//	
	//	cur_factor = (m1 / m2);
	//	global_factor *= cur_factor;

	//	
	//	/*for (int j = 0; j < operations.size(); j = j + 2) {
	//		times[i] = (times[i] - operations[j]) * operations[j + 1];
	//	}
	//	operations.push_back(times[i]);
	//	operations.push_back(cur_factor);*/

	//	time += times[i];
	//	
	//	for (int j = i + 1; j < n; j++) {
	//		times[j] -= times[i];
	//		times[j] *= cur_factor;
	//	}
	//	
	//	
	//	i += count_of_same_files;
	//	count_of_same_files = 1;
	//}
	ofstream file_out("loading.out");
	file_out.setf(ios::fixed);
	file_out.precision(13);
	file_out << time;
	file_out.close();
	//cout << time;
}
