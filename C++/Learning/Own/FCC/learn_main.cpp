#include <iostream>
#include <string>
using namespace std;

int cube(int num){
    return num * num * num;
}

string sayhello(string name = ""){
    return "Hello " + name + "\n";
}

int main(){
    int x = 3;
    cout << sayhello("Farhan");
    cout << cube(6);
}