/**
When Sasha was six, she liked to surprise her elder brother Anton by the following trick.

‘Think of a number,’ Sasha asked.

‘I’m ready.’

‘Now add four.’

‘Well.’

‘Multiply the result by two.’

‘I’ve multiplied.’

‘Subtract the number you have initially thought of.’

‘OK,’ Anton obeyed.

‘Now please add six.’

‘Done.’

‘Subtract your number from the result again.’

‘Ready.’

‘Now it’s time to multiply by three.’

‘Yes.’

‘Concentrate on the number you have got. I’ll try read your mind.’

‘This way? OK, I’m thinking only about the number.’

‘Your final result is…fourty two.’

‘Wow! It’s magic!’ Anton exclaimed.

You are given a sequence of commands. Check if Sasha is able to unambiguously determine the result her brother is going to get after performing all the operations, regardless of the number he has initially thought of. Suppose that Anton does mental arithmetic correctly.

Формат входных данных
The first line of input contains the integer n, the number of commands (0 < n < 20). The commands are written in the next n lines.
add x — add the number x to the current value (where x is an integer ranged from 0 to 99, inclusive, or the ? character that denotes the number that was originally thought of);
subtract x — subtract the number x from the current value (constraints for x are the same);
multiply by y — multiply the current value by y (where y is an integer from 0 to 9).
Формат выходных данных
If the result is definite, output it. If the trick went wrong, output Epic fail.
Примеры
trick.in	trick.out
6
add 4
multiply by 2
subtract ?
add 6
subtract ?
multiply by 3
42
1
add 11
Epic fail


*/

#include <fstream>
#include <iostream>
#include <sstream> 

using namespace std;

int main() {
	
	int n;
	string line;
	ifstream file_in("trick.in");
	getline(file_in, line);
	istringstream iss(line);
	iss >> n;
	string *operations = new string[n];
	for (int i = 0; i < n; i++) {
		getline(file_in, line);
		operations[i] = line;
	}
	file_in.close();

	long long result = 0;
	long long counter_x = 1;
	long long buf = 0;
	for (int i = 0; i < n; i++) {
		istringstream iss(operations[i]);
		iss >> line;
		buf = 0;
		if (line == "add") {
			iss >> line;
			if (line == "?") {
				counter_x++;
			}
			else {
				buf = stoi(line);
				result += buf;
			}
		}
		else if (line == "subtract") {
			iss >> line;
			if (line == "?") {
				counter_x--;
			}
			else {
				buf = -stoi(line);
				result += buf;
			}
		}
		else if (line == "multiply") {
			iss >> line;
			iss >> line;
			buf = stoi(line);
			counter_x *= buf;
			result *= buf;
		}		
	}
	


	ofstream file_out("trick.out");
	if (counter_x != 0) {
		file_out << "Epic fail";
	}
	else {
		file_out << result;
	}
	file_out.close();
	/*for (int i = 0; i < n; i++) {
		cout << operations[i] << endl;
	}*/
	//cout << result;
	//cin >> n;
}