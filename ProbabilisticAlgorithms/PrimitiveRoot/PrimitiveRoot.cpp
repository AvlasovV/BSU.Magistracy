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

int get_primitive_root(int prime){
    int root = prime;


    return root;
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
    }

    input.close();
    output.close();
}
