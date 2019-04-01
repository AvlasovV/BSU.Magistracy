/**
10 Problem 4. Первообразный корень
Input file name: primes.in
Output file name: roots.out
Time limit: 4 s
Memory limit: 1024 MB
Число g называется первообразным корнем по модулю m,
если любое взаимно простое с m число от 0 до m − 1 может быть получено
 путём возведения g в натуральную степень и взятия остатка по модулю m.

Необходимо найти первообразный корень по заданному простому модулю либо сказать, что его не существует.

Input
В первой строке записано число t наборов входных данных (1≤t≤100000).
Каждая из последующих t строк содержит простое число mi (2≤mi≤10^8).
Output
Для каждого числа на входе выведите в отдельной строке первообразный корень по этому модулю,
если он существует, либо −1 в противном случае.
Example
primes.in
3
5
13
89
roots.out
2
2
3
*/

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

// constant for wheel method
long weel_spokes[] = { 1,2,2,4,2,4,2,4,6,2,6 };

int gcd(int a, int b) {
	while (b) {
		a %= b;
		swap(a, b);
	}
	return a;
}

int powmod(int a, int b, int p) {
	int res = 1;
	while (b)
		if (b & 1)
			res = int(res * 1ll * a % p), --b;
		else
			a = int(a * 1ll * a % p), b >>= 1;
	return res;
}


int get_primitive_root(int p) {
	if (p == 2) {
		return 1;
	}
	vector<int> factorization_vector;
	int phi = p - 1;
	int n = phi;
	
	if (n <= 1000000) {
		// simple factorization -- O( sqrt(n) )
		for (int i = 2; i*i <= n; ++i)
			if (n % i == 0) {
				factorization_vector.push_back(i);
				while (n % i == 0)
					n /= i;
			}
		if (n > 1)
			factorization_vector.push_back(n);
	}
	else {
		//	 wheel method
		long f = 2; int w = 0;
		while (f * f <= n) {
			if (n % f == 0) {
				// printf("%ld\n", f);
				factorization_vector.push_back(f);
				n /= f;
			}
			else {
				f += weel_spokes[w];
				w = (w == 10) ? 3 : (w + 1);
			}
		}
		//printf("%ld\n", n);
		if (n > 1)
			factorization_vector.push_back(n);
	}

	for (int k = 0; k < p; ++k) {
		bool ok = true;

		int res = 2 + rand() % (p - 2); // this random part help me to be faster and go through tests in time limit,
										// but if you want to do it right you should remove this line
										// or save passed non-primitive values for not to fall into them twice
		for (size_t i = 0; i < factorization_vector.size() && ok; ++i) 
			ok &= powmod(res, phi / factorization_vector[i], p) != 1;
		
		if (ok) return res;
	}
	return -1;
}



int main(){
    ifstream input("primes.in", std::ifstream::in);
    ofstream output("roots.out");
    int n;
    input >> n;

    int prime;
    int root;
    for (int i = 0; i < n; i++){
        input >> prime;
        root = get_primitive_root(prime);
		output << root << endl;

		//cout << "Root = " << root << endl;
		//cout << "Wheel\n";
		//wheel(prime);
		//cout << endl;

    }

    input.close();
    output.close();
	//cin.get();
}


// fast multiplication as I know but here I use another

//uint64_t mul_mod(uint64_t a, uint64_t b, uint64_t m)
//{
//	long double x;
//	uint64_t c;
//	int64_t r;
//	if (a >= m) a %= m;
//	if (b >= m) b %= m;
//	x = a;
//	c = x * b / m;
//	r = (int64_t)(a * b - c * m) % (int64_t)m;
//	return r < 0 ? r + m : r;
//}
//
//uint64_t pow_mod(uint64_t a, uint64_t b, uint64_t m)
//{
//	uint64_t r = m == 1 ? 0 : 1;
//	while (b > 0) {
//		if (b & 1)
//			r = mul_mod(r, a, m);
//		b = b >> 1;
//		a = mul_mod(a, a, m);
//	}
//	return r;
//}