#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

vector<int> prefix_function(string &s) {
	int n = (int)s.length();
	vector<int> pi(n);

	for (int i = 1; i < n; ++i) {
		int j = pi[i - 1];
		while (j > 0 && s[i] != s[j])
			j = pi[j - 1];
		if (s[i] == s[j])  ++j;
		pi[i] = j;
	}
	return pi;
}


void main() {
	ifstream input_file;
	input_file.open("input.txt");
	int n;
	string s1, s2, s3;
	getline(input_file, s1);
	n = stoi(s1);
	getline(input_file, s1);
	getline(input_file, s2);
	input_file.close();

	ofstream output_file;
	output_file.open("output.txt");

	int index = -1;

	if (s2 != s1) {
		s3 = s2 + "!" + s1 + s1;
		//cout << s1 << "\n";
		vector<int> pi = prefix_function(s3);
		for (size_t i = 2 * n + 1; i < 3 * n + 1; i++)
		{
			if (pi[i] == n) {
				index = i - 2 * n;
				break;
			}
		}
	}
	else {
		index = 0;
	}

	//cout << index;
	/*for (size_t i = 0; i < pi.size(); i++)
	{
		cout << pi[i] << " ";
	}*/
	output_file << index;
	
	//cin.get();



	output_file.close();
}