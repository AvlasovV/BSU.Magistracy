#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <ctime>


using namespace std;


//vector<int> z_function(string s) {
int z_function(string s, int index) {
	vector<int> z(s.length(), 0);
	int l, r = 0;
	int max_value = 0;
	
	for (int i = 1; i < s.length(); i++) {
	//for (int i = index; i >= 0; i--) {
		if (i <= r) {
			z[i] = min(z[i - l], r - i + 1);
		}
		while ((i + z[i] < s.length()) && (s[i + z[i]] == s[z[i]])) {
	//	while ((i + z[i] < index) && (s[i + z[i]] == s[z[i]])) {
			z[i]++;
		}
		if (i + z[i] - 1 > r) {
			l = i; 
			r = i + z[i] - 1;
		}
		
		//getting max_value because of case specification
		if (max_value < z[i]) {
			max_value = z[i];
		}
	}
	//return z;
	return max_value;
}

int reversed_z_function(string &s, int index) {
	vector<int> z(index, 0);
	int l = index, r = index;
	int max_value = 0;

	//for (int i = 1; i < s.length(); i++) {
	for (int i = index-1; i >= 0; i--) {
		if (i >= l) {
			z[i] = min(z[r - i], i - l + 1);
		}
		//while ((i + z[i] < s.length()) && (s[i + z[i]] == s[z[i]])) {
		while ((i - z[i] >= 0) && (s[i - z[i]] == s[index - z[i]])) {
			z[i]++;
		}
		if (i - z[i] - 1 < l) {
			r = i;
			l = i - z[i] - 1;
		}

		//getting max_value because of case specification
		if (max_value < z[i]) {
			max_value = z[i];
		}
	}
	//return z;
	return max_value;
}

int main() {
	//clock_t tStart = clock();

	ifstream input_file;
	input_file.open("input.txt");
	string s;
	getline(input_file, s);
	input_file.close();

	int k = 1;
	for (int i = 1; i < s.length(); ++i) {
		//string substr = s.substr(0, i + 1);
		//cout << substr << endl;
		//reverse(substr.begin(), substr.end());
		//cout << substr << endl << endl;
		int val = reversed_z_function(s, i);
		k += i + 1 - val;
	}
	//cout << k;
	ofstream output_file;
	output_file.open("output.txt");
	output_file << k;
	output_file.close();
	

	//printf("Time taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
}