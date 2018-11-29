/**
The dream of the childhood for Dzianis was to create a new revolutionary operating system. He hasn’t finished his high school yet, but he’s already started working towards this grand goal. Dzianis has prepared a collection of non-boring wallpapers and an icon set, has created a logo of the OS, and has even selected a color for the stop error screen. The only thing that is left is to implement the operating system core. This task seems to be the easiest one from the list above, so Dzianis is not worried about the final success of his startup at all. Nevertheless, he decided to invite you to help him (just for fun, obviously).

The most important entities from the OS perspective are the processes. Each process has a single unique integer associated with it: PID (process identifier). Dzianis wants to reserve zero PID for the kernel and to use 1, 2, 3, … for the other processes. The idea behind the PID managing algorithm is very complex: each time a new process is created, the system finds the smallest available PID and associates it with a new process. Initially all non-reserved PIDs are marked as available, and if some process is terminated, the corresponding PID becomes available again for the new processes if necessary.

You task is to help Dzianis by implementing the PID manager component.

Формат входных данных
The first line of input contains a single integer q (1 ≤ q ≤ 300 000), the number of queries.
The following q lines contain the queries of the following types:

C — create a new process, assign the smallest available PID to it and print this PID to the output;
T i — terminate the process that was created by the i-th ‘create’ query (queries of type C are numbered starting from one) and mark the corresponding PID as a free one.
It is guaranteed that the query sequence is correct and each process is terminated at most once.

Формат выходных данных
For each query of type C, print one line containing a single integer—assigned PID.
Пример
pid.in	
7
C
C
T 1
C
C
T 4
C

pid.out
1
2
1
3
3
*/

#include <fstream>
#include <iostream>
#include <sstream> 
#include <queue>

using namespace std;

class ComparisonClass {
	public:
		bool operator() (int a, int b) {
			return a > b;
		}
};

int main() {

	ifstream input_file("pid.in");
	int n;
	string line;
	getline(input_file, line);
	istringstream iss(line);
	iss >> n;

	priority_queue< int, vector<int>, ComparisonClass > q;
	string *operations = new string[n];
	for (int i = 0; i < n; i++) {
		getline(input_file, line);
		operations[i] = line;
		q.push(i + 1);
	}
	input_file.close();

	
	int counter = 1;
	int* processes = new int[n];
	ofstream output_file("pid.out");
	for (int i = 0; i < n; i++) {
		istringstream iss(operations[i]);
		iss >> line;
		if (line == "C") {
			int top = q.top();
			output_file << top << endl;
			q.pop();
			processes[counter++] = top;
		}
		else if (line == "T") {
			iss >> line;
			q.push(processes[stoi(line)]);
		}

	}
	output_file.close();
}