#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <ctime>


using namespace std;


struct z_func_and_max {
	vector<int> z;
	/*int max_value = 0;
	int max_index = 0;*/
	z_func_and_max(): z(0,0) {};
	z_func_and_max(vector<int> z_vect) : z(z_vect) {};
	//z_func_and_max(vector<int> z_vect, int max_val=0, int max_ind=0) : z(z_vect), max_value(max_val), max_index(max_ind) {};
};

//vector<int> z_function(string s) {
z_func_and_max z_function(string &s, int index=0) {
	vector<int> z(s.length(), 0);
	int l = index, r = index;
	//int max_value = 0, max_index = 0;

	for (int i = index + 1; i < s.length(); i++) {
		if (i <= r) {
			z[i] = min(z[i - l], r - i + 1);
		}
		while ((i + z[i] < s.length()) && (s[i + z[i]] == s[z[i] + index])) {
			z[i]++;
		}
		if (i + z[i] - 1 > r) {
			l = i;
			r = i + z[i] - 1;
		}

		//getting max_value because of case specification
		/*if (max_value < z[i]) {
			max_value = z[i];
			max_index = i;
		}*/
	}
	return z_func_and_max(z);
	//return z_func_and_max(z, max_value, max_index);
	//return max_value;
}


z_func_and_max economical_z_function(string &s, int index = 0) {
	vector<int> z(s.length() - index, 0);
	int l = index, r = index;
	int new_i = 0;
	//int max_value = 0, max_index = 0;

	for (int i = index + 1; i < s.length(); i++) {
		new_i = i - index;
		if (i <= r) {
			z[new_i] = min(z[i - l], r - i + 1);
		}
		while ((i + z[new_i] < s.length()) && (s[i + z[new_i]] == s[z[new_i] + index])) {
			z[new_i]++;
		}
		if (i + z[new_i] - 1 > r) {
			l = i;
			r = i + z[new_i] - 1;
		}

		//getting max_value because of case specification
		/*if (max_value < z[i]) {
			max_value = z[i];
			max_index = i;
		}*/
	}
	return z_func_and_max(z);
	//return z_func_and_max(z, max_value, max_index);
	//return max_value;
}



string get_the_biggest_entry(string &s) {
	vector< vector<int> > z_vec;
	z_func_and_max local_res;
	int max_index = 0;
	int max_length = 0;
	int previous_value = 0;
	int candidate = 0;
	int min_candidate = 0;
	int local_max_value = 0, local_max_index = 0;

	for (auto i = 0; i < s.length(); ++i) {
		local_max_value = 0, local_max_index = 0;
		
		local_res = economical_z_function(s, i);
		z_vec.push_back(local_res.z);
		
		for (size_t k = max_length + 1; k < local_res.z.size(); k++)
		{
			if (local_res.z[k] > local_max_value) {
				local_max_value = local_res.z[k];
				local_max_index = k + i; // add i beacause of offset in the vector, which starts from s[i]
			}
		}
		
		candidate = min(min(local_max_index - i, local_max_value), i);
		if (max_length >= candidate) {
			continue;
		}
		else {
			for (int j = 0; j < i; j++)
			{
				previous_value = z_vec[j][i - j];
				min_candidate = min(min(candidate, i - j), previous_value);
				if (min_candidate > max_length) { // (previous_value >= min_candidate) && 
					max_length = min_candidate;
					max_index = i;
					break;
				}
			}
		}
	
	}
	return s.substr(max_index, max_length);
}


int main() {
	//clock_t tStart = clock();

	ifstream input_file;
	input_file.open("input.txt");
	string s;
	getline(input_file, s);
	input_file.close();

	string result = get_the_biggest_entry(s);

	ofstream output_file;
	output_file.open("output.txt");
	
	output_file << result;

	/*z_func_and_max buf;
	for (size_t i = 0; i < s.length(); i++)
	{
		buf = economical_z_function(s, i);
		for (size_t j = 0; j < buf.z.size(); j++)
		{
			output_file << buf.z[j] << " ";
		}
		output_file << endl;
	}*/

	output_file.close();


	//printf("Time taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
}