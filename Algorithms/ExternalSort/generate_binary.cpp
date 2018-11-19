#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <random>
#include <limits>
#include <algorithm>

using namespace std;

int main() {
    random_device rd;     //Get a random seed from the OS entropy device, or whatever
    mt19937_64 eng(rd()); //Use the 64-bit Mersenne Twister 19937 generator
    //and seed it with entropy.

    //Define the distribution, by default it goes from 0 to MAX(unsigned long long)
    //or what have you.
    uniform_int_distribution<int> distr;

    srand(time(NULL));
	std::ofstream out("input.bin", std::fstream::binary);
    long long n;
    cout << "Enter n" << endl;
    cin >> n;
	out.write((char*)&n, sizeof(long long));
    srand(time(NULL));
	for (int i = 0; i < n; i++) {
        //long long x = distr(eng);
        long long x = rand() % 30;
		out.write((char*)&x, sizeof(x));
	}

	out.close();

	std::ifstream in("input.bin", std::fstream::binary);
	long long n_ = 0;
	in.read((char*)&n_, sizeof(n_));
    long long numbers[n_];

	for (int i = 0; i < n_; i++) {
        long long x = 0;
        in.read((char*)&x, sizeof(x));
        numbers[i] = x;
	}

    sort(numbers, numbers + n_);

    for (int i = 0; i < n_; i++) {
        std::cout << numbers[i] << endl;
    }
    std::cout << std::endl;

	return 0;
}
