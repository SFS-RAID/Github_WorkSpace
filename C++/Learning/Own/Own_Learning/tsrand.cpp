#include <iostream>
#include <random>
#include <stdio.h>
using namespace std;

int main(){
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(1, 10);
    cout << dis(gen) << endl;
}