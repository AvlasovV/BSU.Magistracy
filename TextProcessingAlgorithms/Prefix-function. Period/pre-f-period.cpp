#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

//vector<int> prefix_function(string &s, ofstream &output_file) {
void prefix_function(string &s, ofstream &output_file) {
	int n = (int)s.length();
	vector<int> pi(n);

	int pi_val;
	int len;
	int pref_len;

	for (int i = 1; i < n; ++i) {
		int j = pi[i - 1];
		while (j > 0 && s[i] != s[j])
			j = pi[j - 1];
		if (s[i] == s[j])  ++j;
		pi[i] = j;

		pi_val = pi[i];
		len = i + 1;
		pref_len = len - pi_val;

		if ((pi_val != 0) && (len % pref_len == 0)) {
			//cout << "substr len = " << i+1 << " values: " << pref_len << " " << len / pref_len << endl;
			output_file << len << " " << len / pref_len << "\n";
		}
	}
	/*return pi;*/
}


void main() {
	ifstream input_file;
	input_file.open("input.txt");
	int len;
	string s;
	getline(input_file, s);
	len = stoi(s);
	getline(input_file, s);
	input_file.close();

	ofstream output_file;
	output_file.open("output.txt");

	prefix_function(s, output_file);


	/*cout << s << endl;
	for (size_t i = 0; i < len; i++)
	{
		cout << pi[i] << " ";
	}
	cout << endl;*/

	//int index = len - 1;

	//for (size_t i = 1; i < len; i++)
	//{
	//	int pi_val = pi[i];
	//	int pref_len = i + 1 - pi_val;

	//	if ((pi_val != 0) && ((i + 1) % pref_len == 0)) {
	//		//cout << "substr len = " << i+1 << " values: " << pref_len << " " << (i + 1) / pref_len << endl;
	//		output_file << i + 1 << " " << (i + 1) / pref_len << endl;
	//	}
	//}


	//for (size_t i = len - 1; i > 0; i--)
	//{
	//	index = i;
	//	while (pi[index] != 0) {
	//		index -= pi[index];
	//	}
	//	cout << s.substr(0, index + 1) << endl;
	//}

	//for (size_t i = 0; i < len; i++)
	//{
	//	cout << pi[i] << " ";
	//}
	//

	//cin.get();



	//output_file << result;
	output_file.close();
}