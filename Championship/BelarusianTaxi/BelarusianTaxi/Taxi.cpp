/**
Number plates used for taxi vehicles in the Republic of Belarus have the following format:

region code (a digit from 1 to 7);
three uppercase Latin letters. For the ‘7’ region (Minsk), the combinations TAX, TBX, TEX are used, 
for other regions, only TAX, TBX are currently in use;
a single space;
four-digit number from 1 to 9999, with leading zeroes.


Automatic recognition camera installed over the motorway has read number plates of n vehicles. Determine how many numbers match the format used by Belarusian taxis.

Формат входных данных
The first line of input contains the integer n (1 ≤ n ≤ 100 000). Then, n lines containing the recorded numbers follow. The length of each line is between 3 and 20 characters, it may contain digits, uppercase and lowercase Latin letters, hyphen-minus characters and spaces. Note that all spaces do matter, i. e. if a line has leading or trailing spaces, it may not be a valid taxi number.
Формат выходных данных
Print the number of lines that comply with the rules described above.
Пример
taxi.in	taxi.out
9
7TAX 9215
6TEX 9125
a236ye 73
21-14 BOT
3412 0321 GR
1TBX 0021-7
2-TBX 0001
1TBX 0000
1TBX 0020

Ответ:
2
*/


#include <fstream>
#include <iostream>
#include <sstream> 
#include <vector>
#include <regex>

using namespace std;

int main() {
	
	string pattern1 = "^[1-6][TAX,TBX] [0-9]{3}[1-9]$";
	string pattern2 = "^7[TAX,TBX,TEX] [0-9]{3}[1-9]$";
	regex preg;
	int err, regerr;
	err = regcomp(&preg, pattern1, REG_EXTENDED);

	int n;
	string line;
	ifstream file_in("taxi.in");
	getline(file_in, line);
	istringstream iss(line);
	iss >> n;
	vector <string> plates;
	for (int i = 0; i < n; i++) {
		getline(file_in, line);
		if (line.length() == 9)
			plates.push_back(line);
	}
	file_in.close();

	for (int i = 0; i < plates.size(); i++) {
		cout << plates[i] << "||||" << endl;
	}
	cin >> n;

	ofstream file_out("taxi.out");

	file_out.close();

}