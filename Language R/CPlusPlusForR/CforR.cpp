#include <Rcpp.h>
#include <iostream>
#include <vector>
#include<cmath>

using namespace std;

bool is_prime(long long n){
    bool flag=true;
    for(int i = 2; i <= sqrt(n); i++) {
       if(n % i == 0) {
          flag = false;
          break;
       }
    }
    return flag;
}

// [[Rcpp::export]]
vector<long long> mersen_seq(long long n){
    vector<long long> x;
    x.push_back(1);
    long long two_per_degree = 2;
    while (two_per_degree < n){
        two_per_degree *= 2;
        if(is_prime(two_per_degree - 1)){
            x.push_back(two_per_degree - 1);
        }
    }
    return x;
}

int main(){
    cout << is_prime(100) << endl;
    cout << is_prime(2) << endl;
    cout << is_prime(7) << endl;

    vector<long long> x;
    x = mersen_seq(100);

    for(long long i = 0; i < x.size(); i++){
        cout << x[i] << " ";
    }
}
